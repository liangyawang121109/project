from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from .models import scheduler_table
from django.http import Http404

def index(requests):
    container_list = scheduler_table.objects.all()
    print(container_list)
    template = loader.get_template('scheduler/index.html')
    context = {
        'container_list':container_list,
    }
    return HttpResponse(template.render(context,requests))



