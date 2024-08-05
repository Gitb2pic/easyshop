from django.contrib import admin
from .models import Categories, Products
# Register your models here.

@admin.register(Categories)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
       
@admin.register(Products)
class Categories(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'display','categories', 'stock']