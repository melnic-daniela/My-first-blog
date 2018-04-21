from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    f = open('my_file', 'a+')
    f.write(str(posts))
    f.close()
    return render(request, 'blog/post_list.html', {'posts': posts, 'name': 'Daniela'})