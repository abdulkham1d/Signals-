from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=50)
    users = models.ManyToManyField(User, blank=True, null=True, related_name='phone_numbers')


class Address(models.Model):
    address = models.CharField(max_length=50)
    users = models.ManyToManyField(User, blank=True, null=True, related_name='addresses')