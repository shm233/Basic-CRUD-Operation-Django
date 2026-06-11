from django.shortcuts import render, redirect
from django.db.models import Q
from blogs.models import *

# Create your views here.

def home_view(request):
    blog = BlogModel.objects.all()
    search = request.GET.get('search')
    if search:
        blog = BlogModel.objects.filter(
            Q(title__icontains=search)|
            Q(author_name__icontains=search)|
            Q(content__icontains=search)
        )
    dictionary = {
        'blog': blog
    }
    return render(request, 'home.html', dictionary)

def blog_list(request):
    blog = BlogModel.objects.all()
    
    dictionary = {
        'blog' : blog
    }
    return render(request, 'blog.html', dictionary)

def blog_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author_name')
        content = request.POST.get('content')
        category = request.POST.get('category')
        blog_image = request.FILES.get('blog_image')
        publish_date = request.POST.get('publish_date')
        
        BlogModel.objects.create(
            title = title,
            author_name = author_name,
            content = content,
            category = category,
            blog_image = blog_image,
            publish_date = publish_date
        )
        return redirect('blog_list')        
    return render(request, 'add-blog.html')

def blog_edit(request, b_id):
    blog = BlogModel.objects.get(id = b_id)
    if request.method=='POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author_name')
        content = request.POST.get('content')
        category = request.POST.get('category')
        blog_image = request.FILES.get('blog_image')
        publish_date = request.POST.get('publish_date')
        
        blog.title = title
        blog.author_name = author_name
        blog.content = content
        blog.category = category
        if blog_image:
            blog.blog_image = blog_image
        blog.publish_date = publish_date
        blog.save()
        return redirect('blog_list')
    context = {
        'blog' : blog
    }
    return render(request, 'edit-blog.html', context)

def blog_delete(request, b_id):
    BlogModel.objects.get(id=b_id).delete()
    return redirect('blog_list')
