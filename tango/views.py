from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    text={'fuck':"i want to fuck you bitch"}
    return render(request,'tango/index.html',context=text)
