from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display =['name']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']

@admin.register(Product)
class ProductModeladmin(admin.ModelAdmin):
    list_display = ['name','price', 'category', 'description']

@admin.register(Order)
class OrdertModeladmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'address', 'phone', 'date', 'status']
