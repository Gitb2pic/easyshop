from typing import Iterable
from django.db import models
from django.utils import timezone



class Categories(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
    
class Products(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    display = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Mettre à jour le champ 'display' en fonction de la valeur du stock
        if self.stock > 0:
            self.display = True
        # else:
        #     self.display = False
        super().save(*args, **kwargs)
     
    def __str__(self) -> str:
        return self.name
    
    


