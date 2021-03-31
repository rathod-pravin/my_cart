from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse('<h1>this is shop about page</h1>')

def ProdView(request):
    return HttpResponse('<h1> this is shop product view page...</h1>')

def tracker(request):
    return HttpResponse('<h1> this is shop tracker page...</h1>')

def contact(request):
    return HttpResponse('<h1>this is shop contact us page... </h1>')

def checkout(request):
    return HttpResponse('<h1> this is shop checkout page...</h1>')

