from django.shortcuts import render
from django.http import HttpResponse
import os


def index(request):
    return HttpResponse("Hello Chowder. You are at the poll index!")

def chowder(request):
    return HttpResponse("I am Chowder. Bark Bark Bark Bark. Be careful.")


def serve_chowders_file(request): #open a text file in url
    # Build the path to the file
    file_path = os.path.join(os.path.dirname(__file__), 'static', 'polls', 'myfile.txt')
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Build the path to the file
    return HttpResponse(content, content_type='text/plain')






