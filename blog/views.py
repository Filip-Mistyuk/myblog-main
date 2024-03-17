from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts_list": posts,
    }
    return render(
        request,
        "blog/post_list.html",
        context=context,
    )