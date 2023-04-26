$(document).ready(function(){
   /**
   * Easy selector helper function
   */
   const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }
  /**
   * Countdown timer
   */
  // let countdown = select('.countdown');

  let allClasses= document.querySelectorAll('.container');
  let contValue= Array();

  if(allClasses.length > 0)
  {
    allClasses.forEach(element => {
      contValue.push(element.getAttribute('data-con-id'));
    });



    if(contValue.length > 0)
    {
       contValue.forEach(element => {
       const countDownDate = function() {
         let timeleft = new Date($('.'+element).attr('data-count')).getTime() - new Date().getTime();
         let days = Math.floor(timeleft / (1000 * 60 * 60 * 24));
         let hours = Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
         let minutes = Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60));
         let seconds = Math.floor((timeleft % (1000 * 60)) / 1000);
         
        if(days < 0 || hours < 0)
        {
          $('.'+element).empty().append('<h1> Event Completed </h1>');
          $('.button_'+element).hide();
          $('.button_'+element).empty().append('Expired');
          $('.result_'+element).show();
           
        }else{
          $('.days_'+element).empty().append(days);
          $('.hours_'+element).empty().append(hours);
          $('.min_'+element).empty().append(minutes);
          $('.sec_'+element).empty().append(seconds);
        }
         

       }
       countDownDate();
       setInterval(countDownDate, 1000);
         
       });
    }
  }

});

 