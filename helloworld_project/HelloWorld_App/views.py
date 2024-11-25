from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    return HttpResponse('<h1 style="color:black">{“Message”: “Hello World!”}<h1>')
