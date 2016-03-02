$(document).ready(function() {

    $("#checkboxes input").on('click', function() {
        var $$ = $(this);

        var sel =  $('#checkboxes input:checked');

        if (sel.length > 1) {
            $('#button').prop('disabled', false)
        }
        if (sel.length <= 1) {
            $('#button').prop('disabled', true)
        }
        console.log(sel);
    })

    $("#button").click(function(event) {
       
    })


    $(function() {
        $('#button').click(function(e) {
            event.preventDefault();
            var selected = [];
            $('#checkboxes input:checked').each(function() {
                selected.push($(this).prop('value'));
            });

            //alert(selected);

            var data = {};
            //var posting = $.post('editprof');
            $.ajax({
                url : "/",
                type: "POST",
                data: { name1: selected[0], name2: selected[1] },
                success: function(data, textStatus, jqXHR)
                {
                    
                    console.log(data);
                    $('#graph-row').replaceWith(data);
                    $('#loading-indicator').hide(100);
                    console.log('done');
                    //$('#graph-row').replaceWith(data);
                    
                }
            });
          /*// Put the results in a div
          posting.done(function( data ) {
            var user = $( data ).find( "#usertext" );
            var em = $( data ).find( "#usertext" );
            $("#usernametext").empty().append(user);
            $("#useremailtext").empty().append(em);
          });
        });*/
        });
    });

    jQuery.ajaxSetup({
      beforeSend: function() {
         $('#loading-indicator').show(100);
        console.log('started');
      },
      complete: function(){
         
      },
      success: function() {
        
      }
    });
});