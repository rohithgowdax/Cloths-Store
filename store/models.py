from django.db import models
import datetime

# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)

# All of our products
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(max_length=250, default='', blank=True)
    image = models.ImageField(upload_to='upload/product/')


class Order(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity =models.IntegerField(default=1)
    address =models.CharField(max_length=100, default='', blank=True)
    phone =models.CharField(max_length=10, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)