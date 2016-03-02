#!/usr/bin/env python

import webapp2
import jinja2
import os
import urllib2, urllib
import ast

from google.appengine.ext import vendor
vendor.add('lib')
from twitter import *



sample_t = [0.5306808352470398, 0.8899176716804504, 0.9038220047950745, 0.868643581867218, 0.6827369928359985, 0.8801671266555786, 0.991736114025116, 0.002690057037398219, 0.9336543083190918, 0.5306808352470398, 0.9741988182067871, 0.002868006704375148, 0.010110157541930676, 0.5747017860412598, 0.8998973369598389, 0.8902460336685181, 0.972815215587616, 0.856654942035675, 0.8953496813774109, 0.9682518839836121, 0.6855406761169434, 0.7112892270088196, 0.05528285354375839, 0.6709500551223755, 0.4262143075466156, 0.6164702773094177, 0.5306808352470398, 0.5306808352470398, 0.8863051533699036, 0.8543914556503296, 0.9533530473709106, 0.0117873540148139, 0.986419677734375, 0.9928697347640991, 0.8253277540206909, 0.6075287461280823, 0.16311973333358765, 0.5475262999534607, 0.5405890345573425, 0.09149756282567978, 0.5590296387672424, 0.09416671842336655, 0.7747870087623596, 0.49723759293556213, 0.6699898838996887, 0.784469723701477, 0.4273751974105835, 0.7245113849639893, 0.1709945946931839, 0.020662613213062286, 0.9941648244857788, 0.9456606507301331, 0.9128027558326721, 0.9864793419837952, 0.9585270881652832, 0.9870280623435974, 0.9708049297332764, 0.057380881160497665, 0.02363901399075985, 0.9423059225082397, 0.9635937213897705, 0.9696619510650635, 0.7846164703369141, 0.9643943905830383, 0.04682385176420212, 0.6775093078613281, 0.3205278217792511, 0.46622487902641296, 0.39440324902534485, 0.5386268496513367, 0.8840216398239136, 0.9053995609283447, 0.7078980207443237, 0.014544865116477013, 0.012478342279791832, 0.023547237738966942, 0.007409253623336554, 0.00364784081466496, 0.6037554740905762, 0.8973942995071411, 0.01292111724615097, 0.9398089647293091, 0.9644959568977356, 0.1213492751121521, 0.9410958886146545, 0.8922930359840393, 0.034446150064468384, 0.10121365636587143, 0.9670381546020508, 0.8938319683074951, 0.012741451151669025, 0.3142582178115845, 0.007064353674650192, 0.1388186514377594, 0.7021608352661133, 0.5471625328063965, 0.9343835115432739, 0.772613525390625, 0.8920184373855591, 0.8805136680603027, 0.9898958206176758, 0.9198347926139832, 0.0528721958398819, 0.8774656653404236, 0.964999258518219, 0.9603933691978455, 0.6855747103691101, 0.11121071130037308, 0.986650288105011, 0.8919655084609985, 0.9367422461509705, 0.9960084557533264, 0.4427762031555176, 0.7142332792282104, 0.9263743758201599, 0.6782107353210449, 0.19450201094150543, 0.9790684580802917, 0.7862927317619324, 0.3094022274017334, 0.7715917229652405, 0.3030390739440918, 0.18822866678237915, 0.5521461963653564, 0.9777078628540039, 0.05739063024520874, 0.19598262012004852, 0.7665102481842041, 0.09892203658819199, 0.19181416928768158, 0.8537302017211914, 0.9405806660652161, 0.9710972905158997, 0.03453546389937401, 0.4018774926662445, 0.10824106633663177, 0.9730126261711121, 0.6436184644699097, 0.3867586851119995, 0.3739488124847412, 0.02420816756784916, 0.9818502068519592, 0.36579352617263794, 0.9087400436401367, 0.8986421823501587, 0.08808712661266327, 0.2076866179704666, 0.9093862771987915, 0.21751973032951355, 0.965951144695282, 0.7086003422737122, 0.8948832750320435, 0.5306808352470398, 0.9757114052772522, 0.9320587515830994, 0.3120729923248291, 0.6980164051055908, 0.5102812647819519, 0.5360184907913208, 0.7002632021903992, 0.6019924283027649, 0.12364701181650162, 0.7875313758850098, 0.4083973467350006, 0.9234670400619507, 0.15377318859100342, 0.19484363496303558, 0.8585401773452759, 0.7016815543174744, 0.1071864664554596, 0.9921749234199524, 0.06118350103497505, 0.022446980699896812, 0.9083256721496582, 0.2909250855445862, 0.9401928186416626, 0.9331245422363281, 0.030125007033348083, 0.6099956631660461, 0.48404356837272644, 0.872175395488739, 0.3137919306755066]
sample_h = [0.4432419240474701, 0.663665235042572, 0.8296630382537842, 0.8837041854858398, 0.5419895052909851, 0.47933250665664673, 0.137086421251297, 0.33368298411369324, 0.2550917863845825, 0.7449260950088501, 0.607489824295044, 0.7667655944824219, 0.85325026512146, 0.7849520444869995, 0.9647390246391296, 0.8809610605239868, 0.8988879323005676, 0.9863358736038208, 0.38602975010871887, 0.4976573586463928, 0.3768467903137207, 0.8637233376502991, 0.40578487515449524, 0.7236380577087402, 0.9668758511543274, 0.7565504908561707, 0.8291731476783752, 0.19090388715267181, 0.946557343006134, 0.926463782787323, 0.6223037838935852, 0.8561691641807556, 0.459603875875473, 0.7898433804512024, 0.32653623819351196, 0.43600010871887207, 0.9633227586746216, 0.9162693619728088, 0.47289010882377625, 0.8867705464363098, 0.8732925653457642, 0.0455409437417984, 0.10886714607477188, 0.8177509903907776, 0.8802952170372009, 0.9037907123565674, 0.7656974792480469, 0.8210150599479675, 0.8204247355461121, 0.46455812454223633, 0.37434226274490356, 0.4908079206943512, 0.5068033933639526, 0.43279001116752625, 0.37736988067626953, 0.8691761493682861, 0.7966975569725037, 0.5461096167564392, 0.5983971953392029, 0.32501882314682007, 0.9912267923355103, 0.5704429745674133, 0.9741867780685425, 0.6438379883766174, 0.7473059892654419, 0.70525723695755, 0.9734470844268799, 0.5574151873588562, 0.4738481938838959, 0.8492198586463928, 0.8195556402206421, 0.9691300988197327, 0.837744414806366, 0.4674164950847626, 0.8449006676673889, 0.9642998576164246, 0.8172898888587952, 0.11848229914903641, 0.8768414855003357, 0.42408809065818787, 0.883644163608551, 0.9849448800086975, 0.981586217880249, 0.6124330163002014, 0.00467997882515192, 0.7351317405700684, 0.6945374608039856, 0.8418118953704834, 0.7054605484008789, 0.8550124168395996, 0.8617123365402222, 0.9294320940971375, 0.24603436887264252, 0.7836918830871582, 0.05492021143436432, 0.8492050766944885, 0.3750143349170685, 0.7826324701309204, 0.584962010383606, 0.462900310754776, 0.7636335492134094, 0.6265581250190735, 0.6610922813415527, 0.900194525718689, 0.9673965573310852, 0.9471473097801208, 0.8945572972297668, 0.9317531585693359, 0.4517495632171631, 0.9352619051933289, 0.7758395671844482, 0.18860800564289093, 0.07283128798007965, 0.47111064195632935, 0.8884077072143555, 0.9889330863952637, 0.9713611602783203, 0.8331204652786255, 0.8247838020324707, 0.8493465781211853, 0.8467069864273071, 0.7319092154502869, 0.4121074378490448, 0.7772114872932434, 0.4800473153591156, 0.989029049873352, 0.17596852779388428, 0.9282986521720886, 0.8017832636833191, 0.18568511307239532, 0.49785780906677246, 0.13426926732063293, 0.8550245761871338, 0.7021204829216003, 0.8532611131668091, 0.8913852572441101, 0.14876839518547058, 0.5166928768157959, 0.7875640392303467, 0.33658191561698914, 0.8702059984207153, 0.6119704842567444, 0.7952595949172974, 0.26146072149276733, 0.5216646194458008, 0.7661037445068359, 0.8023487329483032, 0.6945374608039856, 0.6328912973403931, 0.4747518301010132, 0.1518835723400116, 0.6886888146400452, 0.2620910406112671, 0.9007107615470886, 0.7496669292449951]
h_t = [(u'It isn\u2019t right that we have kids trying to learn in crumbling classrooms. We need to invest in neglected communities.', u'Wed Feb 24 13:59:33 +0000 2016'), (u'"[Hillary] tried to help the person that\'s less fortunate.\u201d https://t.co/K0YclxQQbv https://t.co/UEiHiBtOUj', u'Wed Feb 24 18:23:54 +0000 2016'), (u'Proud to have Senator Reid on this team. https://t.co/ZWh9sGcM2T https://t.co/Q3thyUCRFn', u'Wed Feb 24 19:25:43 +0000 2016'), (u"Joining @IAmSteveHarvey today to continue the conversation he's been having on guns in America. Don\u2019t miss it!\nhttps://t.co/fln4WYpSnY", u'Wed Feb 24 20:20:44 +0000 2016'), (u'We\u2019re working to break down barriers for every American by organizing state to state. Follow @HFA for updates from the official campaign!', u'Wed Feb 24 21:08:19 +0000 2016'), (u'Join @AndraDayMusic, @eltonofficial, and @katyperry at @RadioCity for Hillary\u2014get your tickets while they last! https://t.co/9bSXOFxS14', u'Wed Feb 24 21:49:39 +0000 2016'), (u'The Puerto Rican senate just confirmed Maite Oronoz Rodr\xedguez, making her the first LGBT chief justice in the US. https://t.co/EAvYZvoAYu', u'Wed Feb 24 22:50:02 +0000 2016'), (u'A high school student asked Hillary about mental health services for veterans. Her response speaks volumes. https://t.co/0fqFVH1BMZ', u'Thu Feb 25 00:47:47 +0000 2016'), (u'Follow @HFA to hear from the millions of volunteers, supporters, organizers, and donors who power this campaign. https://t.co/Sr6KBZLYqR', u'Thu Feb 25 01:52:03 +0000 2016'), (u'The South Carolina primary is almost here! Ready to stand with Hillary? Say #ImWithHer and commit to vote. https://t.co/mDLrYOTngv', u'Thu Feb 25 13:56:41 +0000 2016'), (u'Mean Tweets: campaign edition with Senator @AlFranken.\nhttps://t.co/F57Uv45SBT', u'Thu Feb 25 17:04:59 +0000 2016'), (u'\u201cWe endorsed her because she endorsed us.\u201d https://t.co/BExsVDdGjb', u'Thu Feb 25 18:48:17 +0000 2016'), (u'"I had to turn my sorrow into a strategy\u2014my mourning into a movement."\nhttps://t.co/SBn8mw43LV', u'Thu Feb 25 20:24:10 +0000 2016'), (u"@transforhillary honored to have your support. Together we'll take a stand for safety, respect, and full equality for trans Americans.", u'Thu Feb 25 21:20:13 +0000 2016'), (u'"Plugged into the establishment matrix?"\n \n"That sounds painful."\n\nMean Tweets with @alfranken:\nhttps://t.co/ffOBjWVo4S', u'Thu Feb 25 22:10:26 +0000 2016'), (u'America never stopped being great. We just need to make it work for everyone. #GOPdebate https://t.co/RiyhfZAAZ1', u'Fri Feb 26 01:45:37 +0000 2016'), (u'The #GOPdebate candidates all hold backward views on LGBT rights, women, and health care. https://t.co/kI3qDwtK4s https://t.co/yae3oHLXUj', u'Fri Feb 26 01:47:01 +0000 2016'), (u'We are not going to deport 12 million people. Demonizing immigrants is beneath our values. #GOPdebate', u'Fri Feb 26 01:49:34 +0000 2016'), (u"Let's break down barriers\u2014not build new walls. #GOPdebate https://t.co/zHs11cLBcC", u'Fri Feb 26 01:55:43 +0000 2016'), (u'We should build a path to citizenship, not a wall on the border. #GOPdebate', u'Fri Feb 26 02:03:56 +0000 2016'), (u"We will not rip families apart. We will defend @POTUS's actions on immigration and go further to keep families together. #GOPdebate", u'Fri Feb 26 02:09:56 +0000 2016'), (u'Como presidenta, Hillary proteger\xe1, renovar\xe1, y expandir\xe1 DACA y DAPA, las \xf3rdenes ejecutivas. No cree en separar a las familias. #GOPdebate', u'Fri Feb 26 02:11:39 +0000 2016'), (u"We need comprehensive immigration reform to keep families like Karla's together. #GOPdebate\nhttps://t.co/hd6FCPv7mW", u'Fri Feb 26 02:14:06 +0000 2016'), (u'.@POTUS is doing his job to fill the vacancy on the Supreme Court. @marcorubio, @tedcruz, and GOP senators should do theirs. #GOPdebate', u'Fri Feb 26 02:25:59 +0000 2016'), (u"Planned Parenthood provides critical health care to millions of Americans. Republicans vow they'll defund it. Not on our watch. #GOPdebate", u'Fri Feb 26 02:34:43 +0000 2016'), (u'Affordable health care should be a human right in America, not a privilege. We will not let Republicans repeal the ACA. #GOPdebate', u'Fri Feb 26 02:40:35 +0000 2016'), (u"What will strengthen our economy: raising middle-class incomes.\n\nWhat won't: more tax cuts for millionaires. \n\n#GOPdebate", u'Fri Feb 26 02:52:16 +0000 2016'), (u"We can't let Republicans rip away @POTUS\u2019 progress. Text ImWithHer to 47246 if you agree.", u'Fri Feb 26 02:59:20 +0000 2016'), (u'We live in a world with serious foreign policy challenges. We need serious leadership. #GOPdebate https://t.co/dKnVM7wB85', u'Fri Feb 26 03:15:15 +0000 2016'), (u'No matter which Republican is nominated, we can\u2019t afford to let him in the White House. Add your name if you agree. https://t.co/pGL3xPDce8', u'Fri Feb 26 03:49:15 +0000 2016'), (u"This is it: Your last chance to say you're with Hillary before the South Carolina primary! Commit today. https://t.co/LQ9PdocLWa", u'Fri Feb 26 14:00:01 +0000 2016'), (u"It's been less than a week since a mass shooting tore apart a community, and now another. This has to end. Praying for Hesston, KS. -H", u'Fri Feb 26 16:53:27 +0000 2016'), (u"Let's not divide ourselves between \u201cus\u201d and \u201cthem.\u201d America works better when we all do our part. We\u2019re in this together.", u'Fri Feb 26 18:00:14 +0000 2016'), (u'Talking sexism in the workplace, racial justice, and...perspiration with @Buzzfeed\u2019s @AnotherRound. https://t.co/ByNDVR4JNl', u'Fri Feb 26 18:45:00 +0000 2016'), (u'"She cares. She tries. She perseveres." @jonfavs on supporting Hillary in 2016: https://t.co/uW2g9VJuuY', u'Fri Feb 26 20:01:57 +0000 2016'), (u'What\u2019s at stake in this election is whether or not we\u2019re going to help every kid reach their potential.\nhttps://t.co/EDwrkmqZlm', u'Fri Feb 26 20:35:54 +0000 2016'), (u'Living without discrimination should be a right for all, not a privilege for some. Hear hear, @AbbyWambach. https://t.co/Amwn4r43xt', u'Fri Feb 26 21:34:06 +0000 2016'), (u"Obamacare saved this woman when she needed emergency surgery. Let's build on its progress, not start over.\nhttps://t.co/TPMaxuk6lN", u'Fri Feb 26 22:26:00 +0000 2016'), (u"It's outrageous that students are being asked to pay interest rates higher than you would pay to buy a house.\nhttps://t.co/yTOUBVi82w", u'Fri Feb 26 23:33:51 +0000 2016'), (u".@marcorubio standing up for banks instead of hardworking citizens is wrong. It's time to put Puerto Ricans first. https://t.co/ilFSV4SRL1", u'Sat Feb 27 00:59:32 +0000 2016'), (u'Hillary no le aumentar\xe1 los impuestos a la clase media. Cuando la clase media es fuerte, el pa\xeds es fuerte.', u'Sat Feb 27 02:32:32 +0000 2016'), (u'Sometimes running for president involves crashing a bachelor party. https://t.co/0I5Txpq34x', u'Sat Feb 27 03:19:38 +0000 2016')]
t_t = [(u'Great new poll. Thank you Texas! #VoteTrump #MakeAmericaGreatAgain https://t.co/VHqAvsIyuW', u'Thu Feb 25 04:07:19 +0000 2016'), (u'Mitt Romney, who was one of the dumbest and worst candidates in the history of Republican politics, is now pushing me on tax returns. Dope!', u'Thu Feb 25 12:34:11 +0000 2016'), (u'Why doesn\u2019t @MittRomney just endorse @marcorubio already.\nShould have done it before NH or Nevada where he had a little sway. Too late\nnow!', u'Thu Feb 25 16:05:01 +0000 2016'), (u'Just for your info, tax returns have 0 to do w/ someone\u2019s net worth. I have already filed my financial statements w/ FEC. They are great!', u'Thu Feb 25 16:22:44 +0000 2016'), (u"Signing a recent tax return- isn't this ridiculous? https://t.co/UdwqF4iZIZ", u'Thu Feb 25 16:35:12 +0000 2016'), (u'LETS MAKE AMERICA GREAT AGAIN!\nSchedule &amp; tickets: https://t.co/nU39QHzxxX https://t.co/GUQo1TMsMo', u'Thu Feb 25 16:41:37 +0000 2016'), (u"I'm going to do what @MittRomney was totally unable to do- WIN!", u'Thu Feb 25 16:44:52 +0000 2016'), (u'Join me in Oklahoma tomorrow night!\n#MakeYoutubeGreatAgain #Trump2016\nhttps://t.co/sUTcDoip3C', u'Thu Feb 25 17:41:26 +0000 2016'), (u'Thank you Illinois! #Trump2016 https://t.co/Ol0u2Krkwc', u'Thu Feb 25 17:49:48 +0000 2016'), (u"Early on Ted Cruz said that if he didn't win South Carolina, it's over. He didn't win- and lost to me in a landslide!", u'Thu Feb 25 18:58:03 +0000 2016'), (u'FMR PRES of Mexico, Vicente Fox horribly used the F word when discussing the wall. He must apologize! If I did that there would be a uproar!', u'Thu Feb 25 20:27:15 +0000 2016'), (u'THANK YOU!  \n#MakeAmericaGreatAgain #Trump2016\nhttps://t.co/nvgOPoo5qf https://t.co/0JCjfbcpJZ', u'Thu Feb 25 22:16:26 +0000 2016'), (u"Failed presidential candidate @MittRomney was made to look like a fool by Senator Harry Reid &amp; didn't release his tax returns until 9/21/12.", u'Fri Feb 26 05:40:07 +0000 2016'), (u'Thank you! WE WILL MAKE AMERICA GREAT AGAIN! #Trump2016 https://t.co/aht7wYVIUg', u'Fri Feb 26 05:53:13 +0000 2016'), (u'#MakeAmericaGreatAgain!  https://t.co/in4raBhwqa', u'Fri Feb 26 06:08:56 +0000 2016'), (u'Thank you! #GOPDebate Polls \n#MakeAmericaGreatAgain https://t.co/At5vOiLCSy', u'Fri Feb 26 06:49:51 +0000 2016'), (u'#MakeAmericaGreatAgain #Trump2016 https://t.co/FvIUXMkrjj', u'Fri Feb 26 06:52:24 +0000 2016'), (u'All the online polls have me winning the debate. I really enjoyed the evening. Not easy, but good. https://t.co/sLTmwVVM5I', u'Fri Feb 26 06:54:44 +0000 2016'), (u'Big day in Texas tomorrow! Having a rally in Fort Worth. Tremendous crowd. Will be exciting! #Trump2016 https://t.co/JGUopujRIk', u'Fri Feb 26 06:55:35 +0000 2016'), (u'"@morg25016893:  @eventbrite Also, all the things Rubio&amp;Cruz were using for hits, just petty. Trump, clearly the only one w/all the skills."', u'Fri Feb 26 07:33:59 +0000 2016'), (u'"@Indies4Trump: Vote Early in the #LoneStarState #SuperTuesday @realDonaldTrump will #MakeAmericaGreatAgain https://t.co/GC8kmWFxoM"', u'Fri Feb 26 07:34:58 +0000 2016'), (u'"@Slytle24: @davidaxelrod @realDonaldTrump @CNN he won almost all polls and Mark Halperin gave him an A-', u'Fri Feb 26 07:38:29 +0000 2016'), (u'"@restorereality: Tonight you proved to America you are the real deal. You took fire from all sides, stayed composed, returned fire and WON!', u'Fri Feb 26 12:25:39 +0000 2016'), (u'"@SkylerDeckard: @realDonaldTrump "that\'s because you\'ve never hired anyone to do work before" favorite line from tonights debate."', u'Fri Feb 26 12:27:33 +0000 2016'), (u'"@tdltdltdltdl:  Marco Cruz and Ted Rubio (easy to get the two politicians confused) looked like desperate, panicked DC insiders tonight"', u'Fri Feb 26 12:28:58 +0000 2016'), (u'"@donell27743094: @realDonaldTrump trump won the debate. Disgusting Rubio said "peed" - is he still in junior high school."', u'Fri Feb 26 12:29:42 +0000 2016'), (u'"@MJP1370: @realDonaldTrump Cruz talks about Hillary all the time because he knows he can\'t beat you ! Trump will win Texas !"', u'Fri Feb 26 12:29:59 +0000 2016'), (u'"@WaltSeher: @realDonaldTrump @morg25016893 @eventbrite yup 200 Polish immigrants were hired by his contractor not Trump"', u'Fri Feb 26 12:30:24 +0000 2016'), (u'I will be making a speech at 12:00 in Fort Worth, Texas. Really big crowd expected. Will be talking about the debate last night-plus, plus!', u'Fri Feb 26 13:56:30 +0000 2016'), (u'Have a good chance to win Texas on Tuesday. Cruz is a nasty guy, not one Senate endorsement and, despite talk, gets nothing done. Loser!', u'Fri Feb 26 14:02:29 +0000 2016'), (u'Why would the people of Florida vote for Marco Rubio when he defrauded them by agreeing to represent them as their Senator and then quit!', u'Fri Feb 26 14:49:40 +0000 2016'), (u'Will be at Fort Worth (Texas) Convention Center at 11:30 A.M. Big crowd - get there early! Big announcement to be made!', u'Fri Feb 26 16:07:56 +0000 2016'), (u'Lying Ted Cruz and lightweight choker  Marco Rubio teamed up last night in a last ditch effort to stop our great movement. They failed!', u'Fri Feb 26 16:15:06 +0000 2016'), (u'Lightweight choker Marco Rubio looks like a little boy on stage. Not presidential material!', u'Fri Feb 26 16:16:14 +0000 2016'), (u'Wow, every poll said I won the debate last night. Great honor!', u'Fri Feb 26 16:17:29 +0000 2016'), (u'Lightweight Marco Rubio was working hard last night. The problem is, he is a choker, and once a choker, always a choker! Mr. Meltdown.', u'Fri Feb 26 16:38:36 +0000 2016'), (u"They don't like Rubio in Florida- he left them high &amp; dry. Doesn't even show up for votes!", u'Fri Feb 26 20:52:02 +0000 2016'), (u'Thank you for your support &amp; \nfriendship- Governor @ChrisChristie!\n#MakeAmericaGreatAgain #Trump2016 https://t.co/jVI6Q6JH18', u'Fri Feb 26 21:07:16 +0000 2016'), (u'Never let them see you sweat! https://t.co/qygVFf6JFF', u'Fri Feb 26 21:11:30 +0000 2016'), (u'Thank you Texas! 10,000 amazing \nsupporters! #Trump2016 \n#MakeAmericaGreatAgain https://t.co/T2cBdktPbp', u'Fri Feb 26 21:34:21 +0000 2016'), (u'What I would do on my first day in office. #MakeAmericaGreatAgain\nWatch: https://t.co/DhANDG8uBd https://t.co/SzdZzYOnDG', u'Sat Feb 27 02:08:18 +0000 2016'), (u'"@donnieboysmith: @realDonaldTrump in contrast to Rubio and Cruz you look like a giant. They look terribly weak" Thank you!', u'Sat Feb 27 03:08:53 +0000 2016'), (u'"@itsblakec: @realDonaldTrump Trump is a genius. Rubio and Cruz are not. I want a brilliant mind to run this country."', u'Sat Feb 27 04:53:34 +0000 2016'), (u'"@JerryJrFalwell: A majority of evangelicals believe @realDonaldTrump is best equipped to save the country. #Greta"', u'Sat Feb 27 04:58:32 +0000 2016'), (u'Thank you Pastor Robert Jeffress! #MakeAmericaGreatAgain #Trump2016 https://t.co/ndKu8m8RY2', u'Sat Feb 27 05:06:27 +0000 2016')]


#INIT TEMPLATE DIRECTORY
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):  #write out a string to browser
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params): #given a template and parameters, renders and returns a string with 
		t = jinja_env.get_template(template) #gets template
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class HomeHandler(Handler):
	def get(self):
		self.render("homepage.html")

	def post(self):
		name1 = self.request.get('name1')
		name2 = self.request.get('name2')
		
		print name1
		print name2


		count = 50
		tweets1 = get_tweets(name1, count)
		tweets2 = get_tweets(name2, count)
		result1 = []
		result2 = []
		#s = ""
		for t in tweets1:
			result1.append((ast.literal_eval(get_sent_indico(t[0])))['results'])

		for t in tweets2:
			result2.append((ast.literal_eval(get_sent_indico(t[0])))['results'])

		# name1="realDonaldTrump"
		# name2="HillaryClinton"
		# result1 = sample_h
		# result2	= sample_t

		print "****** Number of tweets" + name1 + ": " + str(len(result1)) + " ***********"
		print "****** Number of tweets" + name2 + ": " + str(len(result2)) + " ***********"
		

		pos1 = movingAverageExponential(result1, 0.97, epsilon = 0)
		pos2 = movingAverageExponential(result2, 0.97, epsilon = 0)
		
		lables = get_labels(min(len(pos1), len(pos2)))
		
		for i in range(len(pos1)):
			pos1[i] = int(100 * pos1[i])

		for i in range(len(pos2)):
			pos2[i] = int(100 * pos2[i])

		
		per1 = get_personality(h_t)
		per2 = get_personality(t_t)

		for i in range(len(per1)):
			per1[i] = int(100 * per1[i])

		for i in range(len(per2)):
			per2[i] = int(100 * per2[i])

		self.render('data.html', pos_data1 = pos1, pos_data2 = pos2, per_data1 = per1, per_data2 = per2, lables = lables, name1=name1, name2=name2)


def get_tweets(username, count):
	# load our API credentials 
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

def get_sent_indico(tweet):
	url = "http://apiv2.indico.io/sentimenthq?key=6f464b828f2061cfbf6021e5113af555"
	params = {'data': tweet}
	data = urllib.urlencode(dict([k.encode('utf-8'),unicode(v).encode('utf-8')] for k,v in params.items()))
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	return response.read()

def get_personality_indico(tweet):
	url = "http://apiv2.indico.io/personality?key=6f464b828f2061cfbf6021e5113af555"
	params = {'data': tweet}
	data = urllib.urlencode(dict([k.encode('utf-8'),unicode(v).encode('utf-8')] for k,v in params.items()))
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	return response.read()

def get_labels(count):
	l = []
	for i in range(1, count + 1):
		l.append(i)
		#l.append("1")
	return l

def moving_average(data, interval):
	running_av= []
	sum_t = 0
	count = 1;
	for item in data:
		sum_t += item
		av = sum_t/count
		if(count == interval):
			running_av.append(av)
			count = 0
			sum_t = 0
		count += 1
	return running_av



# Returns a list of personality traits after analyzing all tweets
def get_personality(tweets):
	openness = 0
	conscientiousness = 0
	extraversion = 0
	agreeableness = 0

	for t in t_t:
		pers = get_personality_indico(t[0])
		pers_d = ast.literal_eval(pers)
		pers_d = pers_d['results']
		openness += pers_d['openness']
		conscientiousness += pers_d['conscientiousness']
		extraversion += pers_d['extraversion']
		agreeableness += pers_d['agreeableness']

	return [openness/len(tweets), conscientiousness/len(tweets), extraversion/len(tweets), agreeableness/len(tweets)]

#Source: http://stackoverflow.com/questions/488670/calculate-exponential-moving-average-in-python
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
