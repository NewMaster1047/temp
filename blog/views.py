from django.shortcuts import render
from .models import Post, Comment, LikePost, FollowUser


def home_view(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'signup.html')
