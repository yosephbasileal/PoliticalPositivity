#!/usr/bin/env python

# Import libraries
import webapp2
import jinja2
import os
import urllib2, urllib
import ast

from google.appengine.ext import vendor
vendor.add('lib')
from twitter import *

# Init template directory
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)

# Main handler class
class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):  # write out a string to browser
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template) # gets template
		return t.render(params) # render template with parameters

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))


# Handler for homepage
class HomeHandler(Handler):
	def get(self):
		self.render("homepage.html")

	def post(self):
		# get name of selected candidates
		name1 = self.request.get('name1')
		name2 = self.request.get('name2')
		
		# output for debugging
		print name1
		print name2

		# number of recent tweet to analyze
		count = 50

		# get tweets of both candidates
		tweets1 = get_tweets(name1, count)
		tweets2 = get_tweets(name2, count)
		
		# analyze positivity of all tweets
		result1 = []
		result2 = []
		for t in tweets1:
			result1.append((ast.literal_eval(get_sent_indico(t[0])))['results'])

		for t in tweets2:
			result2.append((ast.literal_eval(get_sent_indico(t[0])))['results'])

		# output for debugging
		print "****** Number of tweets" + name1 + ": " + str(len(result1)) + " ***********"
		print "****** Number of tweets" + name2 + ": " + str(len(result2)) + " ***********"
		
		# build a running average of the data
		pos1 = movingAverageExponential(result1, 0.97, epsilon = 0)
		pos2 = movingAverageExponential(result2, 0.97, epsilon = 0)
		
		# determine the size of the x-axis labels based on the minimum of the two 
		lables = get_labels(min(len(pos1), len(pos2)))
		
		# scale positivity data by 100
		for i in range(len(pos1)):
			pos1[i] = int(100 * pos1[i])

		for i in range(len(pos2)):
			pos2[i] = int(100 * pos2[i])

		# get personality traits from tweets
		per1 = get_personality(tweets1)
		per2 = get_personality(tweets2)

		# scale personality data by 100
		for i in range(len(per1)):
			per1[i] = int(100 * per1[i])

		for i in range(len(per2)):
			per2[i] = int(100 * per2[i])

		# redner page
		self.render('data.html', pos_data1 = pos1, pos_data2 = pos2, per_data1 = per1, per_data2 = per2, lables = lables, name1=name1, name2=name2)


# Returns the recent tweets of the desired user
# Source: https://github.com/ideoforms/python-twitter-examples
def get_tweets(username, count):
	# load API credentials 
	config = {}
	execfile("config.py", config)

	# create twitter API object
	twitter = Twitter(
			auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

	# this is the user we're going to query.
	user = username

	# query the user timeline.
	results = twitter.statuses.user_timeline(screen_name = user, count = count, include_rts = False)

	# loop through each status item, and print its content.
	tweets = []
	for t in results:
		#print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))
		#print status["text"]
		tweets.append((t["text"], t["created_at"]))

	tweets.reverse()
	#print tweets
	return tweets


# Returns sentiment analysis of a tweet by sending to indico server
def get_sent_indico(tweet):
	url = "http://apiv2.indico.io/sentimenthq?key=6f464b828f2061cfbf6021e5113af555"
	params = {'data': tweet}
	data = urllib.urlencode(dict([k.encode('utf-8'),unicode(v).encode('utf-8')] for k,v in params.items()))
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	return response.read()


# Returns personality analysis of a tweet by sending to indico server
def get_personality_indico(tweet):
	url = "http://apiv2.indico.io/personality?key=6f464b828f2061cfbf6021e5113af555"
	params = {'data': tweet}
	data = urllib.urlencode(dict([k.encode('utf-8'),unicode(v).encode('utf-8')] for k,v in params.items()))
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	return response.read()


# Get x-axis labels for the positivity graph, for now just numbers 1-count
def get_labels(count):
	l = []
	for i in range(1, count + 1):
		l.append(i)
	return l


# Returns a list of personality traits after analyzing all tweets
def get_personality(tweets):
	# initialize variables
	openness = 0
	conscientiousness = 0
	extraversion = 0
	agreeableness = 0

	# for each tweet
	for t in tweets:
		pers = get_personality_indico(t[0])
		pers_d = ast.literal_eval(pers)
		pers_d = pers_d['results']
		openness += pers_d['openness']
		conscientiousness += pers_d['conscientiousness']
		extraversion += pers_d['extraversion']
		agreeableness += pers_d['agreeableness']

	# combine all traits into a list
	return [openness/len(tweets), conscientiousness/len(tweets), extraversion/len(tweets), agreeableness/len(tweets)]


# Get an exponential running average of data
# Source: http://stackoverflow.com/questions/488670/calculate-exponential-moving-average-in-python
def movingAverageExponential(values, alpha, epsilon = 0):

   if not 0 < alpha < 1:
      raise ValueError("out of range, alpha='%s'" % alpha)

   if not 0 <= epsilon < alpha:
      raise ValueError("out of range, epsilon='%s'" % epsilon)

   result = [None] * len(values)

   for i in range(len(result)):
       currentWeight = 1.0

       numerator     = 0
       denominator   = 0
       for value in values[i::-1]:
           numerator     += value * currentWeight
           denominator   += currentWeight

           currentWeight *= alpha
           if currentWeight < epsilon: 
              break

       result[i] = numerator / denominator

   return result


app = webapp2.WSGIApplication([
	('/', HomeHandler)
], debug=True)
