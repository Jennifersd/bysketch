from django.db import models
# from django.core.urlresolvers import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    FRAMEWORKCSS_CHOICES = (
        ('Bootstrap_4', 'Bootstrap_4'),
        ('Bluma', 'Bluma')
    )

    FRAMEWORKJS_CHOICES = (
        ('Vue', 'Vue'),
        ('Angular', 'Angular'),
        ('React', 'React')
    )

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=False)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    background = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    document = models.FileField(upload_to='downloads/%Y/%m/%d', blank=True)
    version_free = models.FileField(upload_to='downloads/%Y/%m/%d', blank=True)
    version_premium = models.FileField(upload_to='downloads/%Y/%m/%d', blank=True)
    free = models.BooleanField(default=False)
    support = models.BooleanField(default=False)
    documentation = models.BooleanField(default=False)
    framework_css = models.CharField(max_length=14, choices=FRAMEWORKCSS_CHOICES, default='bluma')
    framework_js = models.CharField(max_length=14, choices=FRAMEWORKJS_CHOICES, default='bluma')
    components = models.DecimalField(max_digits=10, decimal_places=0, default=False)
    examples_pages = models.DecimalField(max_digits=10, decimal_places=0, default=False)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=False)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

        