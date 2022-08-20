from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def file(request):
    return render(request,"add.html")
def add(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    result=x+y
    result1=x-y
    result2=x*y
    result3=x/y
    return render(request,"result.html",{'result':result,'result1':result1,'result2':result2,'result3':result3})
