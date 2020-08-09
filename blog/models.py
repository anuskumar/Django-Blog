from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
	# A custom Manager extending the base Manager
	# Overriding the base QuerySet get_queryset() method, returns all posts with the published status
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')

	# A method count_published() returns the number of posts with published status
	def count_published(self):
		return super(PublishedManager, self).get_queryset().filter(status='published').count()

class AuthorManager(models.Manager):
	# A custom Manager extending the base Manager
	# A method active_author_posts() returns all the posts written by authors currently active
	def active_author_posts(self):
		return super(AuthorManager, self).get_queryset().filter(author__is_active=True)

class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title 	= models.CharField(max_length=250)
	slug	= models.SlugField(max_length=250, unique_for_date='publish')
	author	= models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	body	= models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status 	= models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	# The default manager named objects renamed to posts. Multiple managers can be created.
	# Usage: Posts.posts.all()
	# posts = models.Manager()
	
	# Usage: Post.objects.active_author_posts()
	objects = AuthorManager()
	# Usage: Post.published.all() and Post.objects.count_published()
	published = PublishedManager()

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

