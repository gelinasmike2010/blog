from django.shortcuts import render
from .models import Post
from django.views import generic

from django.views.generic import TemplateView

class BaseView(TemplateView):
    template_name = "base.html"

# class PostView(generic.ListView):
#         model = Post
