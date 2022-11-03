from django.shortcuts import render

def index(request):
    context = {
        'judul': 'web',
        'heading': 'selamat datang',
    }

    return render(request, 'index.html', context)