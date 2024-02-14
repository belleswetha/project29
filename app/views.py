from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse


# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse ( 'data is entered') 
        else:
            return ('data is invalid')

    return render(request,'insert_topic.html',d)


def insert_Webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            To=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']
            wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=u,email=e)[0]
            wo.save()
            return HttpResponse('data is entered')
        else:
            return('data is invalid')
        
    return render(request,'insert_Webpage.html',d)
   
def insert_Access(request):
    EAFO=AcessForm()
    d={'EAFO':EAFO}
    if request.method=="POST":
        ARFDO=AcessForm(request.POST)
        if ARFDO.is_valid():
            wn=ARFDO.cleaned_data['name']
            wo=Webpage.objects.get(name=wn)
            d=ARFDO.cleaned_data['date']
            a=ARFDO.cleaned_data['author']
            ao=AcessRecords.objects.get_or_create(name=wo,date=d,author=a)[0]
            ao.save()
            return HttpResponse('data is inserted')

        else:
            return('data is invalid')
        
    return render(request,'insert_access.html',d)