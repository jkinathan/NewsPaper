from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import  DeleteView, UpdateView
from .models import Article
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied # new
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ArticleCreateView(LoginRequiredMixin,CreateView):
    template_name = "article_create.html"
    model = Article
    fields = ('title','body')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ArticleListView(LoginRequiredMixin,ListView):
    template_name = "article_list.html"
    model = Article
    login_url = 'login'    
    
class ArticleDetailView(LoginRequiredMixin,DetailView):
    template_name = "article_detail.html"
    model = Article
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "article_edit.html"
    fields = ('title', 'body')
    model = Article
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        
        if obj.author != self.request.user:
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)
    
class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    template_name = "article_delete.html"
    model = Article
    success_url = reverse_lazy('article_list')
    login_url = 'login' 
    
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        
        if obj.author != self.request.user:
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)