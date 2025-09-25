from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    price_before=models.DecimalField(max_digits=10,decimal_places=2)
    price_after=models.DecimalField(max_digits=10,decimal_places=2)
    dis=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
    @property
    def price(self):
        return self.price_after
