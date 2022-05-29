from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse



def index(request):
    return render(request,"products/index.html",{})
