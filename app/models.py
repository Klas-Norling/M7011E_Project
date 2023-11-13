from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


class Super_User(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)


class Admin(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)


class Category(models.Model):
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Product(models.Model):
    category = models.OneToOneField("category", on_delete=models.PROTECT)
    price = models.IntegerField()
    stock = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Special_Sale(models.Model):
    name = models.CharField(max_length=255)


class Product_Discount(models.Model):
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    special_sale = models.OneToOneField("Special_Sale", on_delete=models.PROTECT)
    discount = models.IntegerField()


class Review(models.Model):
    product = models.OneToOneField("Product", on_delete=models.PROTECT)
    user = models.OneToOneField("User", on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    score = models.IntegerField()

class Order(models.Model):
    user = models.OneToOneField("User", on_delete=models.PROTECT)
    payment_status = models.CharField(max_length=255)
    order_date = models.CharField(max_length=255)
    total_price = models.IntegerField()
    status = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)


class Order_Item(models.Model):
    product = models.OneToOneField("Product", on_delete=models.PROTECT)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()