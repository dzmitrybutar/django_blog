from django.shortcuts import render
from django.http import HttpResponse

def posts_list(request):
    return HttpResponse('<h1>hello<h1>')

