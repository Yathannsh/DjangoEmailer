from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.shortcuts import render

# new imports that go at the top of the file
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

import smtplib
import string

def index(request):
     return HttpResponseRedirect('/newsletter/contact')

def success(request):
	#if request.method == 'GET':
	#	message = 'You submitted: %r' % request.GET.get('name')%
	#else:
	#	message = 'You submitted nothing!'
	#return HttpResponse(message)
	return render(request, 'success.html')
	
# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
            })
            content = template.render(context)

            USER    = 'raxydots@gmail.com'
            PASS    = 'raxysharma'
            HOST    = 'smtp.gmail.com'
            SUBJECT = "Welcome newsletter"
            TO      = contact_email
            FROM    = "admin@dotsquares.com"
            TEXT    = 'Thanks for subscribing newsletter '+contact_name
            message = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
            
            
            server = smtplib.SMTP(HOST)
            server.starttls()
            server.set_debuglevel(1)
            server.login(USER, PASS)
            server.sendmail(FROM, TO, message)
            server.quit()
			#return HttpResponseRedirect('/newsletter/success?name='+contact_name)
            return HttpResponseRedirect('/newsletter/success')

    return render(request, 'contact.html', {
        'form': form_class,
    })