from django.db import models

# Create your models here.

class Details(models.Model):
    CATEGORY_ID = models.CharField(max_length=5, null=True, blank=True)
    Categories = models.CharField(max_length=25, null=True, blank=True)
    ITEM_ID = models.CharField(max_length=9, null=True, blank=True)
    ENGLISH_NAME = models.CharField(max_length=25, null=True, blank=True)
    PRICE = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self):
        return self.ENGLISH_NAME