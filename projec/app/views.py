from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    return render(request, "home.html")

