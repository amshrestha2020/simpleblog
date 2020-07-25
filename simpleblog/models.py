from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Pending"),
    (3, "Accepted"),
    (4, "Rejected")
)

def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id   = str(instance.author.id), 
        title       = str(instance.title),
        filename    = filename
    )
    return file_path

class Category(models.Model):
    name              =  models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    title             =  models.CharField(max_length=255)
    title_tag         =  models.CharField(max_length=255)
    author            =  models.ForeignKey(User, on_delete=models.CASCADE)
    body              =  RichTextField(blank=True, null=True)
    # body              =  models.TextField()
    image             =  models.ImageField(upload_to=upload_location, null=False, blank=False)
    status            =  models.IntegerField(choices=STATUS, default=0)
    category          =  models.CharField(max_length=255, default="coding")
    snippet           =  models.CharField(max_length=255)
    likes             =  models.ManyToManyField(User, related_name="blog_posts")
    created_at        =  models.DateTimeField(default=timezone.now, verbose_name="created at")
    updated_at        =  models.DateTimeField(default=timezone.now, verbose_name="updated at")
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse('home')

class Profile(models.Model):
    profile_pic       =  models.ImageField(null=True, blank=True)
    user              =  models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username          =  models.CharField(max_length=255)
    bio               =  models.TextField()
    first_name        =  models.CharField(max_length=255)
    last_name         =  models.CharField(max_length=255)
    website_url       =  models.CharField(max_length=255, null=True, blank=True)
    facebook_url      =  models.CharField(max_length=255, null=True, blank=True)
    instagram_url     =  models.CharField(max_length=255, null=True, blank=True)
    linkedIn_url      =  models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post             =  models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name             =  models.CharField(max_length=255)
    body             =  models.TextField()
    date_added       =  models.DateTimeField(default=timezone.now, verbose_name="date added")

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
