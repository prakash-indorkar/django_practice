from django.shortcuts import render, redirect
from .forms import UserRegisterForm
'''from django.contrib.auth.forms import UserCreationForm'''
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html',{'form':form})