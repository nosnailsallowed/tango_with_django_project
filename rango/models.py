<<<<<<< HEAD
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def _str_(self): # For Python 2 use _unicode too
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharFiels(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
=======
from django.db import models

# Create your models here.
>>>>>>> 3ff2dfde0f87c58d4c2d510f8e463658dda9e569
