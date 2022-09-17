from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'edusys_app/home.html')

def signup(request):
    return render(request, 'edusys_app/signup.html', {'form':UserCreationForm()})
