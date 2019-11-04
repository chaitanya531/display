from django.http import *
from django.shortcuts import render
def home1(request):
    return render(request,'home.html')
def display1(request):
    text1=request.GET['text1']
    text2=request.GET['text2']
    if text1=='sai':
        text3='sai your details are'
        return render(request,'display.html',{'text1':text1,'text2':text2,'text3':text3})
    else:
         text3='raj your details are'
         return render(request,'display2.html',{'text1':text1,'text2':text2,'text3':text3})

