from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def biryani(request):
    return render(request,'biryani.html')

def chicken(request):
    return HttpResponse('<center><h1>Chicken is very Spicy</h1><br/><h2>This is String Response</h2></center>')