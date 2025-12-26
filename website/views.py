from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    return HttpResponse("home_page")
def about_view(request):
    return HttpResponse("about_page")
def contact_view(request):
    return HttpResponse("contact_page")
