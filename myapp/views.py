from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest

def first(request):
    # return HttpRequest("hihhhhhhhhh")
    return render(request,)

def akhil(request):
    return render(request, 'sample1.html')