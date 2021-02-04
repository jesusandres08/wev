from theblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.

#def home(request):
    #return render(request, 'theblog/home.html', {})

class HomeView(ListView):
    model   =   Post
    template_name   =   'theblog/home.html'
    ordering=['-post_date']

class ArticleDetailView(DetailView):
    model   =   Post
    template_name   =    'theblog/article_details.html'

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='theblog/add_post.html'
    #fields='__all__'
    

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='theblog/update_post.html'
    #fields=['title','title_tag','body']
    
class DeletePostView(DeleteView):
    model=Post
    template_name='theblog/delete_post.html'
    #fields=['title','title_tag','body']
    
    success_url=reverse_lazy('home')

