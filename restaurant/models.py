from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=255)
    No_of_guest=models.BigIntegerField()
    BookingDate=models.DateTimeField()
class Booking(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    inventory=models.IntegerField()


    
