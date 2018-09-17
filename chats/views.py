from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Person, Post, Comment

# Create your views here.
def index(request):
    data = Post.objects.order_by('title')
    context = {'list_post': data}
    return render(request, 'chats/index.html', context)