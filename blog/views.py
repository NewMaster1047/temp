from django.shortcuts import render
from .models import Post, Comment, LikePost, FollowUser


def home_view(request):
    posts = Post.objects.filter(is_published=True)
    data = {'posts': posts}

    return render(request, 'index.html', context=data)


def login_view(request):
    return render(request, 'signup.html')






