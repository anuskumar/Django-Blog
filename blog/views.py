from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from .models import Post

def post_list(request):
	posts 		= Post.published.all()
	paginator 	= Paginator(posts, 1)
	page 		= request.GET.get('page')
	try:
		if int(page)<=0:
			posts 	= paginator.page(1)
		elif int(page)>=paginator.num_pages:
			posts 	= paginator.page(paginator.num_pages)
		else:
			posts 	= paginator.page(page)
	except PageNotAnInteger:
		posts 	= paginator.page(1)
	except EmptyPage:
		posts 	= paginator.page(paginator.num_pages)
	except:
		posts 	= paginator.page(1)
	context		= {
		'posts': posts,
	}
	print(posts.previous_page_number)
	return render(request, 'blog/post/list.html', context)

def post_detail(request, year, month, day, slug):
	post 	= get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
	context	= {
		'post': post,
	}
	return render(request, 'blog/post/detail.html', context)
