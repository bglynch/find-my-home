from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return HttpResponse('<h1>Account Register</h1>')


def my_account(request):
    return HttpResponse('<h1>Account my account</h1>')
