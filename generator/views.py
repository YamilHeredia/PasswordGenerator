from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request): 
    return render(request, 'generator/about.html')

def password(request):

    caracteres =  list('abcdefghijklmnopqrstuvwxyz')
    generatedPassword = ""

    length = int(request.GET.get('length')) 

    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKMNOPQRSTUVWXYZ')) 

    if request.GET.get('especial'):
        caracteres.extend(list('!"#$%&/()'))

    if request.GET.get('numeros'):
        caracteres.extend(list('1234567890'))          

    for x in range(length):
        generatedPassword += random.choice(caracteres)
    
    return render(request, 'generator/password.html', {'password': generatedPassword})