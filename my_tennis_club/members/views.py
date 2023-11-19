from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

def members(request):
    mymembers = models.Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    mymember = models.Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context,request))

# Create your views here.

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())