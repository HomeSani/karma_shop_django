from django.db import models
from django.contrib.auth.models import User

from .const import COLORS

class Brends(models.Model):
    name = models.CharField(max_length=256, verbose_name="Name")

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=256, verbose_name="Name")

    def __str__(self):
        return self.name

class Sneakers(models.Model):
    name = models.CharField(max_length=256, verbose_name="Name")
    description = models.CharField(max_length=512, verbose_name="Description")
    price = models.PositiveIntegerField(default=10, verbose_name="Price in $")
    width = models.PositiveIntegerField(verbose_name="Width in mm")
    height = models.PositiveIntegerField(verbose_name="Height in mm")
    depth = models.PositiveIntegerField(verbose_name="Depth in mm")
    weight = models.PositiveIntegerField(verbose_name="Weight in gm")
    freshness_duration = models.PositiveIntegerField(verbose_name="Freshness Duration in days")
    is_avalible = models.BooleanField(default=False, verbose_name="Is avalibe")
    brend = models.ForeignKey(Brends, on_delete=models.CASCADE, related_name="sneakers")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="sneakers")
    color = models.CharField(max_length=32, choices=COLORS, verbose_name="Color of sneaker")

    def __str__(self):
        return f"{self.name} - {self.price}"

class Reviews(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="reviews")
    text = models.CharField(max_length=300)
    rating = models.PositiveIntegerField(default=1)
    sneaker = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.author}({self.sneaker}): {self.text}"
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="carts")
    sneaker = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name="sneakers")

    def __str__(self):
        return f"Cart of {self.user}"