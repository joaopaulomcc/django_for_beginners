from blog_app.models import Post
from django.shortcuts import render
from django.views.generic import DetailView, ListView


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"