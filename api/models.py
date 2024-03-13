from django.db import models

# Create your models here.
class Company(models.Model):
     Company_id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=50)
     location=models.CharField(max_length=50)
     about=models.TextField()
     type=models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),
                                                 ('Mobile Phones',
                                                  'Mobile Phones')))
     added_date=models.DateTimeField(auto_now=True)
     active=models.BooleanField(default=True)
     class Meta:
          managed=True

class Employee(models.Model):
     name=models.CharField(max_length=100)
     email=models.CharField(max_length=50)
     address=models.CharField(max_length=200)
     phone=models.CharField(max_length=15)
     about=models.TextField()
     position=models.CharField(max_length=50, choices=(('Manager','Manager'),
                                                       ('Software Developer','Software Developer'),
                                                       ('Project Manager','project Manager')
                                                       ))
     Company=models.ForeignKey(Company,on_delete=models.CASCADE)
     class Meta:
          managed=True
 