from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('i am wanna playing dota 2')

def home(request):
    return render(request, 'home.html', {'welcome': 'key'})