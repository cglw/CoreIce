from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

from Ice import MongoOperator


def index(request):
    return render(request, "home.html")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    print(MongoOperator.MongoOperator.db)
    return HttpResponse(str(c))
