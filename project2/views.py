from django.http import *
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def display1(request):
    text1=request.GET['text1']
    text2=request.GET['text2']
    if text1=='Admin':
       if text2=='admin':
           return render(request,'display.html',{'text1':text1,'text2':text2})
       else :
           return render(request,'home.html')  
    elif text1=='User1':
        if text2=='user1':
           return render(request,'display2.html',{'text1':text1,'text2':text2})
        else:
           return render(request,'home.html')
    else :
        return render(request,'home.html')
