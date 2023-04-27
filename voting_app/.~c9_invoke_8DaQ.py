
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Enquiry, Events, Options, Transactions
from django.contrib.auth.models import User
import string
from random import choice
from pollstats import views as statistics


def index(request):
    # list= {'two','three','four','five','six','seven','eight','nine','ten'}

    # for i in list:
    #     email= 'testuser'+i+'@gmail.com'
    #     u=User(password= '123456', email= email, username= email,is_superuser=1,is_active=1, date_joined= '2023-04-22 09:20:19')
    #     u.save()
    events = Events.objects.all()
    message=""
    status="none"
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']   
        e = Enquiry(email=email, message=message)
        e.save()
        status="success"
        message="Message Sent Successfully"

    return render(request, 'voting_app/index.html', {'message': message, 'status': status, 'events': events})

def compare_dates(d1, d2):
    d1_y = d1.year
    d1_m = d1.month
    d1_d = d1.day
    d2_y = d2.year
    d2_m = d2.month
    d2_d = d2.day
    if d1_y > d2_y:
        return d1
    elif d1_y < d2_y:
        return d2
    else:
        if d1_m > d2_m:
            return d1
        elif d1_m < d2_m:
            return d2
        else:
            if d1_d > d2_d:
                return d1
            elif d1_d < d2_d:
                return d2

def host_event_page(request):
    msg_flag = -1
    if request.method == 'POST':
        msg_flag = 0
        event_name = request.POST['event_name']
        event_description = request.POST['event_description']
        event_code = request.POST['event_code']
        referal_code = request.POST['referal_code']
        starting_date = request.POST['starting_date']
        starting_date_processing = starting_date.replace('T', '-').replace(':', '-').split('-')
        starting_date_processing = [int(v) for v in starting_date_processing]
        starting_date_processing_out = datetime.datetime(*starting_date_processing)
        ending_date = request.POST['ending_date']
        ending_date_processing = ending_date.replace('T', '-').replace(':', '-').split('-')
        ending_date_processing = [int(v) for v in ending_date_processing]
        ending_date_processing_out = datetime.datetime(*ending_date_processing)
        # import current date
        curr_date = datetime.datetime.now()
        event_status = 0
        # compare current date with starting and ending date :
        # if curr_date > start_date && curr_date > end_date --> event_status=-1
        if compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==curr_date:
            event_status = -1 
        # if curr_date < start_date && curr_date < end_date --> event_status=1
        elif compare_dates(curr_date, starting_date_processing_out)==starting_date_processing_out and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
            event_status = 1 
        # if curr_date > start_date && curr_date < end_date --> event_status=0
        elif compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
            event_status = 0 
        choice = request.POST['choice']
        if(choice == 'two'):
            o1_name = request.POST['field_one']
            o1_event = request.POST['event_code']
            o2_name = request.POST['field_two']
            o2_event = request.POST['event_code']
            o1 = Options(option_name=o1_name, event_code=o1_event)
            o2 = Options(option_name=o2_name, event_code=o2_event)
            o1.save()
            o2.save()
        if(choice == 'three'):
            o1_name = request.POST['field_one']
            o1_event = request.POST['event_code']
            o2_name = request.POST['field_two']
            o2_event = request.POST['event_code']
            o3_name = request.POST['field_three']
            o3_event = request.POST['event_code']
            o1 = Options(option_name=o1_name, event_code=o1_event)
            o2 = Options(option_name=o2_name, event_code=o2_event)
            o3 = Options(option_name=o3_name, event_code=o3_event)
            o1.save()
            o2.save()
            o3.save()
        if(choice == 'four'):
            o1_name = request.POST['field_one']
            o1_event = request.POST['event_code']
            o2_name = request.POST['field_two']
            o2_event = request.POST['event_code']
            o3_name = request.POST['field_three']
            o3_event = request.POST['event_code']
            o4_name = request.POST['field_four']
            o4_event = request.POST['event_code']
            o1 = Options(option_name=o1_name, event_code=o1_event)
            o2 = Options(option_name=o2_name, event_code=o2_event)
            o3 = Options(option_name=o3_name, event_code=o3_event)
            o4 = Options(option_name=o4_name, event_code=o4_event)
            o1.save()
            o2.save()
            o3.save()
            o4.save()
        if(choice == 'five'):
            o1_name = request.POST['field_one']
            o1_event = request.POST['event_code']
            o2_name = request.POST['field_two']
            o2_event = request.POST['event_code']
            o3_name = request.POST['field_three']
            o3_event = request.POST['event_code']
            o4_name = request.POST['field_four']
            o4_event = request.POST['event_code']
            o5_name = request.POST['field_five']
            o5_event = request.POST['event_code']
            o1 = Options(option_name=o1_name, event_code=o1_event)
            o2 = Options(option_name=o2_name, event_code=o2_event)
            o3 = Options(option_name=o3_name, event_code=o3_event)
            o4 = Options(option_name=o4_name, event_code=o4_event)
            o5 = Options(option_name=o5_name, event_code=o5_event)
            o1.save()
            o2.save()
            o3.save()
            o4.save()
            o5.save()
        if(choice == 'six'):
            o1_name = request.POST['field_one']
            o1_event = request.POST['event_code']
            o2_name = request.POST['field_two']
            o2_event = request.POST['event_code']
            o3_name = request.POST['field_three']
            o3_event = request.POST['event_code']
            o4_name = request.POST['field_four']
            o4_event = request.POST['event_code']
            o5_name = request.POST['field_five']
            o5_event = request.POST['event_code']
            o6_name = request.POST['field_six']
            o6_event = request.POST['event_code']
            o1 = Options(option_name=o1_name, event_code=o1_event)
            o2 = Options(option_name=o2_name, event_code=o2_event)
            o3 = Options(option_name=o3_name, event_code=o3_event)
            o4 = Options(option_name=o4_name, event_code=o4_event)
            o5 = Options(option_name=o5_name, event_code=o5_event)
            o6 = Options(option_name=o6_name, event_code=o6_event)
            o1.save()
            o2.save()
            o3.save()
            o4.save()
            o5.save()
            o6.save()
        user_email = request.POST['user_email']
        confirm_password = request.POST['confirm_password']
        # confirm_username = request.POST['confirm_username
        if User.objects.get(password=confirm_password, email=user_email):
            u = User.objects.get(password=confirm_password, email=user_email)
            e = Events(event_name=event_name, event_code=event_code, event_status=event_status, referal_code=referal_code, hosted_by=u, event_description=event_description, starting_date=starting_date, ending_date=ending_date)
            e.save()
            msg_flag = 1    
    return render(request, 'voting_app/host_event_page.html', {'msg_flag': msg_flag})

def participate_to_vote(request):
    flag = 0
    msg_flag = 0
    if request.method == 'POST':
        uname = request.POST['uname']
        password =  request.POST['password']
        event_code = request.POST['event_code']
        referal_code = request.POST['referal_code']
        u = User.objects.get(username=uname, password=password)
        e = Events.objects.filter(event_code=event_code, referal_code=referal_code) 
        if not e.exists():
            msg_flag = -1
        else:
            trans = Transactions.objects.filter(voter=u, event_code=event_code, referal_code=referal_code) 
            if trans:
                flag = -1
            else:
                return redirect('event_page', event_code)
    return render(request, 'voting_app/participate_to_vote.html', {'msg_flag': msg_flag, 'flag': flag})

def event_page(request, event_code):
    if not request.user.is_authenticated:
        return redirect('/')
    event = Events.objects.get(event_code=event_code)
    starting_date_processing_out = event.starting_date
    ending_date_processing_out = event.ending_date
    curr_date = datetime.datetime.now()
    event_status = 0
    if compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==curr_date:
        event_status = -1 
    elif compare_dates(curr_date, starting_date_processing_out)==starting_date_processing_out and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
        event_status = 1 
    elif compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
        event_status = 0 
        
    event.event_status = event_status
    event.save()  
    options = Options.objects.filter(event_code=event_code)
    total_count = 0
    percs = []
    for option in options:
        total_count += option.count
    max_vote = 0
    winner = ''
    for option in options:
        if option.count > max_vote:
            max_vote = option.count
            winner = option.option_name
    msg_flag = 0
    option_error_flag=0
    voted_for=''
    slugged_name= ''

    # check if the the user has alredy voted
    email= request.user.email
    password= request.user.password
    u = User.objects.get(email=email, password=password)
    t = Transactions.objects.filter(voter=u, event_code=event.event_code, referal_code=event.referal_code)
    if t.exists():
       msg_flag = -1
       for info in t:
        voted_for= info.option_name
        slugged_name= voted_for.replace(' ','_')   

    if request.method == 'POST':
        if 'option' not in request.POST:
         option_error_flag=1
        else:
         option_name = request.POST['option']
         email = request.POST['email']
         password = request.POST['password']

         u = User.objects.get(email=email, password=password)
         tr = Transactions(voter=u, option_name=option_name, event_name=event.event_name, event_code=event.event_code, referal_code=event.referal_code)
         tr.save()
         # increment count by 1 :
         op = Options.objects.get(option_name=option_name, event_code=event_code)
         op.count = op.count + 1
         op.save()
         msg_flag = 1
         return redirect('event_page', event_code)
    
    return render(request, 'voting_app/event_page.html', {'event_code': event_code, 'event': event, 'total_count': total_count, 'options': options, 'percs': percs, 'winner': winner, 'msg_flag': msg_flag, 'option_error_flag':option_error_flag,'voted_for':voted_for,'slugged_name':slugged_name})

def view_event(request, event_code):
    event = Events.objects.get(event_code=event_code)
    starting_date_processing_out = event.starting_date
    ending_date_processing_out = event.ending_date
    curr_date = datetime.datetime.now()
    event_status = 0
    if compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==curr_date:
        event_status = -1 
    elif compare_dates(curr_date, starting_date_processing_out)==starting_date_processing_out and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
        event_status = 1 
    elif compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
        event_status = 0 
    event.event_status = event_status
    event.save()  
    options = Options.objects.filter(event_code=event_code)
    total_count = 0
    percs = []
    for option in options:
        total_count += option.count
    max_vote = 0
    winner = ''
    for option in options:
        if option.count > max_vote:
            max_vote = option.count
            winner = option.option_name
    return render(request, 'voting_app/view_event.html', {'event_code': event_code, 'event': event, 'total_count': total_count, 'options': options, 'percs': percs, 'winner': winner})


def dashboard(request):
    events = Events.objects.all()
    transactions = Transactions.objects.all()
    return render(request, 'voting_app/dashboard.html', {'events': events, 'transactions': transactions})

def manage_events(request):
    events = Events.objects.all()
    return render(request, 'voting_app/view_events.html', {'events':events})

def edit_event(request, event_id):
    event_info= Events.objects.get(id=event_id)
    starting_date= datetime.date.strftime(event_info.starting_date, "%Y-%m-%d")
    ending_date= datetime.date.strftime(event_info.ending_date, "%Y-%m-%d")

    if request.method == 'POST':
       event_name= request.POST['event_name']
       starting_date= request.POST['starting_date']
       ending_date= request.POST['ending_date']

       event_info.event_name= event_name
       event_info.starting_date= starting_date
       event_info.ending_date= ending_date
       event_info.save()

       return redirect('/edit_event/'+event_id)
    
    return render(request, 'voting_app/edit_events.html', {'event_info':event_info,'s_date':starting_date,'e_date':ending_date,'event_id':event_id})

def unvote(request, event_code,voted_for):
    user_id= request.user.id
    Transactions.objects.filter(event_code= event_code, voter_id= user_id).delete()

    # subtract the vote from options
    voted_for= voted_for.replace('_',' ')
    options_data=Options.objects.get(event_code= event_code,option_name= voted_for)
    current_vote_count= options_data.count
    if current_vote_count > 0:
     new_vote_count= (current_vote_count-1)
     options_data.count= new_vote_count
     options_data.save()

    return redirect('/event_page/'+event_code)

def delete_event(request, event_id):
    Events.objects.filter(id= event_id).delete()
    return redirect('/manage_events')

def create_campaign(request):
    
    if request.method == 'POST':
        chars = string.digits
        random =  ''.join(choice(chars) for _ in range(4))
        event_name= request.POST['event_name']
        event_description= 'description'
        event_status= 0
        starting_date= request.POST['starting_date']
        ending_date= request.POST['ending_date']
        event_code= random
        referal_code= event_code
        hosted_by_id= request.user.id

        # save event data
        event_data= Events(event_name=event_name,event_code=event_code,referal_code=event_code, hosted_by_id=request.user.id,event_description=event_description, event_status=event_status, ending_date=ending_date,starting_date=starting_date)
        event_data.save()

        # save options data
        option_one_name= request.POST['option_one']
        option_two_name= request.POST['option_two']

        options_date= Options.objects.bulk_create([
            Options(option_name=option_one_name,count=0, event_code=event_code),
            Options(option_name=option_two_name,count=0, event_code=event_code)
        ])

        return redirect('/manage_events')

    return render(request, 'voting_app/create_campaign.html',{})

def stats(req):
   
   events= Events.objects.filter()
   data= {}
   for e in events:
    # get stats for each event iteration
    data[e.id]= statistics.getusernumbers(e.event_code,e.id)
   print(data)
   
   return render(req, 'voting_app/stats.html',{'event_info':events, 'votes_data':data})


    
