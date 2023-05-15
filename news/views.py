from django.shortcuts import render
from .models import news

def all_news(request):
    mynews=news.objects.order_by('-date')[:2]
    return render(request,'news/all_news.html',{'news':mynews})