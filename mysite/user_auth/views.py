from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import RegisterForm

def register(request):

    if request.method == 'POST':
        response = HttpResponse()
        response.write("<h1>Thank for registering</h1><br>")
        response.write("Your name :" + request.POST['username'] + "</br>")
        response.write("Your email: " + request.POST['email'] + "</br>")
        return response

    registerForm = RegisterForm()
    return render(request, 'user_auth/register.html',{'form': registerForm})