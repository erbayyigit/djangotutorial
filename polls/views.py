from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello Chowder. You are at the poll index!")

def chowder(request):
    return HttpResponse("I am Chowder. Bark Bark Bark Bark. Be careful")