from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    name = 'Привет'
    context = {'name': 'Влад'}
    return render(request, 'base.html', context)