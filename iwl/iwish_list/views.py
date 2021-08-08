from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Item
# Create your views here.


def index(request):
    items_list = Item.objects.order_by('?')

    template = loader.get_template('iwish_list/index.html')
    context = {
        'items_list': items_list,
    }
    return HttpResponse(template.render(context, request))
