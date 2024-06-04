from django.shortcuts import render, redirect
from .forms import ExampleForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def home(request):
    form = ExampleForm()
    return render(request,'index.html', {'form':form})

def contact(request):
	if request.method == 'POST':
		form = ExampleForm(request.POST)
		if form.is_valid():
			# subject = "Contact" 
			# try:
			# 	send_mail(subject, 'hi', 'admin@example.com', ['admin@example.com']) 
			# except BadHeaderError:
			# 	return HttpResponse('Invalid header found.')
			return redirect ("home")
      
	form = ExampleForm()
	return render(request, "contact.html", {'form':form})
