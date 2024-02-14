from django import forms

from app.models import *

class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)


class WebpageForm(forms.Form):
    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()

class AcessForm(forms.Form):
    wl=[[ wo.name,wo.name] for wo in Webpage.objects.all()]
    name=forms.ChoiceField(choices=wl)
    date=forms.DateField()
    author=forms.CharField()



