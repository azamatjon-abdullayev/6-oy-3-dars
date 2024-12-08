from django.shortcuts import render
from .models import *
# Create your views here.

def home(malumot):
    courses = Course.objects.all()
    return render(malumot,'index.html',{"courses":courses})