from django.shortcuts import get_object_or_404, render
from .models import Post

def post_list(request):
	posts 	= Post.published.all()
	context	= {
		'posts': posts,
	}
	return render(request, 'blog/post/list.html', context)

def post_detail(request, year, month, day, slug):
	post 	= get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
	context	= {
		'post': post,
	}
	return render(request, 'blog/post/detail.html', context)
