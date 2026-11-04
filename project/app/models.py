# from django.db import models
#
# class Booking(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()
#     address = models.TextField()
#     members = models.IntegerField()
#     days = models.IntegerField()
#
#     gender_choices = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     )
#     gender = models.CharField(max_length=10, choices=gender_choices)
#
#     payment_choices = (
#         ('Cash', 'Cash'),
#         ('Card', 'Card'),
#         ('UPI', 'UPI'),
#     )
#     payment_method = models.CharField(max_length=20, choices=payment_choices)
#
#     id_proof = models.FileField(upload_to='idproofs/')
#
#     def __str__(self):
#         return self.name
# # Create your models here.
from django.db import models

class Booking(models.Model):

    # CUSTOMER DETAILS
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    image=models.ImageField(upload_to='idproofs/',null=True,blank=True)
    # BOOKING DETAILS
    members = models.IntegerField()
    days = models.IntegerField()
    ROOM_CHOICES = (
        ('Single Room', 'Single Room'),
        ('Deluxe Room', 'Deluxe Room'),
        ('Suite Room', 'Suite Room'),
    )
    room_type = models.CharField(max_length=50, choices=ROOM_CHOICES)

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    PAYMENT_CHOICES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('UPI', 'UPI'),
    )
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)

    id_proof = models.FileField(upload_to='idproofs/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self.name