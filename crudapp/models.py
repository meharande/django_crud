from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField('First Name', max_length=255, blank=True, null=True)
    last_name = models.CharField('Last Name', max_length=255, blank=True, null=True)
    phone = models.CharField('Phone', max_length=20, blank=True, null=True)
    email = models.EmailField('Email')
    address = models.TextField('Address', blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)
    created_at = models.DateTimeField('Careated At', auto_now_add=True)

    def __str__(self):
        return self.first_name

class Articles(models.Model):
    title = models.CharField('Title', max_length=255, blank=True, null=True)
    description = models.TextField()

