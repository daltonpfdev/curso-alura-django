from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World</h1><p>Bem vindo ao Espaço</p>")

