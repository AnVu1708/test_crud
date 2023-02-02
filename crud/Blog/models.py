from django.db import models

class Blog(models.Model):
    BlogId = models.CharField(max_length=30)
    Title = models.CharField(max_length=200)
    Author_Name = models.CharField(max_length=300)
    Start_Date = models.DateField()
    End_Date = models.DateField()
class Category(models.Model):
    CategoryID= models.CharField(max_length=30)
    name = models.CharField(max_length=250)
    def __str__(self):
        return str(self.name)
class Product(models.Model):
    ProductID= models.CharField(max_length=30)
    Product_Name= models.CharField(max_length=250)
    Product_Prices = models.CharField(max_length=250)
    Product_CategoryID= models.ForeignKey(
          Category, 
          on_delete=models.CASCADE)
    class Meta:
        db_table = 'Blog'
