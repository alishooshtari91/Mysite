from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    return render(request,template_name="website/index.html")
def about_view(request):
    return render(request,template_name="website/about.html")
def contact_view(request):
    return render(request,template_name="website/contact.html")
