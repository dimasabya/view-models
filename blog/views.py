from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'judul': 'blog',
        'heading': 'selamat datang di blog',
        'post': posts
    }

    return render(request, 'blog/index.html', context)