from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')         #an additional [:4] sorts the blogs by latest date and shows only 4 of 'em.
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})


def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog':blog})
