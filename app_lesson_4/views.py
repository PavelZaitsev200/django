from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_lesson_4(requests):
    return HttpResponse('Домашка по 4 занятию')
