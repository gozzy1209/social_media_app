from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Profile

# Create your views here.

@Login_required(login_url='signin')
def index(request):
    return render(request,'index.html')

def signup(request):
    #request is an object that represents an HTTP request made by a client (usually a web browser) to the server
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                #then redicet to setting page

                #create a profile for the new user
                user_model = User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,id=user_model.id)
                new_profile.save()
                return redirect('login')


        else:
            messages.info(request, 'password not matching')
            return redirect('signup')


    return render(request,'signup.html')

def signin(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login (request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
        
    return render(request,'signin.html')

@Login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')
