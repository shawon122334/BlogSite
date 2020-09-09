from django.shortcuts import render
from .models import Post
posts = [
    {
        'author' : 'shawon',
        'title' : 'blog post 1',
        'content' : 'first post content',
        'date' : '28 july 2020',
    }, {
        'author' : 'sabbir',
        'title' : 'blog post 2',
        'content' : 'second post content',
        'date' : '29 july 2020',
    }

]

def home(request):
    contex={
        'post': Post.objects.all()
    }
    return render(request,'blog/home.html',contex)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})