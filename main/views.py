import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth import logout


from .models import *

def index(request):
  
    banner = Page.objects.filter(slug="welcome-banner").first()
    return render(request, "index.html", 
            {
            'banner':banner
            } )

def page(request, slug):
    ''
    page = Page.objects.filter(slug=slug).first()
    return render(request, "page.html", {'page': page,} )

def do_logout(request):
    logout(request)

    return redirect("/")
