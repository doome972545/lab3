from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsPost
# Create your views here.


def index(request):
    NewsPosts = NewsPost.objects.all()
    return render(request,'index.html',{'x': NewsPosts})