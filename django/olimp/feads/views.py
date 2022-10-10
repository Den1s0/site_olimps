from re import S
from django.shortcuts import render
from .models import Post
def olimp_list(request):
    olimps = Post.objects.all()
    s = []
    for olimp in olimps:
        if 'inf' in olimp.tags:
            s.append('olimp')
    return render(request, 'feads/olimp_lists.html')