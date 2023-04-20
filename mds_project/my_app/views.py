from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def User(request):
    return HttpResponse("<h1>User Page</h1>")