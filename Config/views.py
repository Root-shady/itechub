from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = 'index.html'
