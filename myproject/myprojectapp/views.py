from django.shortcuts import render
from django.http import HttpResponse
from . models import place


# Create your views here.
def file(request):
    obj=place.objects.all
    return render(request,"index.html",{'table':obj})
#def about(request):
    #return render(request,"about.html")
#def contact(request):
    #return render(request,"contact.html")
#def details(request):
    #return render(request,"details.html")
#def thanks(request):
    #return render(request,"thanks.html")
def add(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    result=x+y
    result1=x-y
    result2=x*y
    result3=x/y
    return render(request,"result.html",{'result':result,'result1':result1,'result2':result2,'result3':result3})
