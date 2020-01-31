from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('This is My First Django View')
    return render(request, 'home_page.html', {})