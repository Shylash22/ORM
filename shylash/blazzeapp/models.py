from django.db import models
from django.contrib import admin
class CustomerDB(models.Model):
    Customerid=models.IntegerField(primary_key=True);
    Name=models.CharField(max_length=10);
    Address=models.CharField(max_length=30);
    Email=models.EmailField();
    DoB=models.DateField();
    Mobile_no=models.IntegerField();
         
class StudentDBAdmin(admin.ModelAdmin):
	list_display=['Customerid','Name','Address','Email','DoB','Mobile_no'];


