from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from edusys_app.forms import RegistrationForm

# Create your views here.

def home(request):
    """Вызов домашней страницы"""
    return render(request, 'edusys_app/home.html')

def signupuser(request):
    """Регистрация пользователей"""
    if request.method == 'GET':
        return render(request, 'edusys_app/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
            except IntegrityError:
                return render(request, 'edusys_app/signupuser.html', {'form': UserCreationForm(), 'error': 'Это имя уже занято'})
        else:
            return render(request, 'edusys_app/signupuser.html', {'form':UserCreationForm(), 'error':'Пароли не совпадают'})

def register(request):
    """Кастомная форма регистрации пользователей"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    #Доделать исключения
    else:
        # form = RegistrationForm()
        # args = {'form': form}
        # return render(request, )
        pass

def logoutuser(request):
    """Выход пользователя"""
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    """Вход пользователя в учётную запись"""
    if request.method == 'GET':
        return render(request, 'edusys_app/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'edusys_app/loginuser.html', {'form': AuthenticationForm(), 'error':'Имя и пароль не совпадают'})
        else:
            login(request, user)
            return redirect('home')