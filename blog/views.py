from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    per_page = request.GET.get('per_page', 5)
    paginator = Paginator(posts, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'per_page': per_page})