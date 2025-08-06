from django.db import models


# Create your models here.
DepartmentsList = [
    ('Hr','Hr'),
    ('Sales','Sales'),
    ('Marketing','Marketing'),
]
Role = [
    ('Manager','Manager'),
    ('Cashier','Cashier'),
    ('admin','Admin'),
]
Resident = [
    ('Ug','Ug'),
    ('Tz','Tz'),

]
class Department(models.Model):
    Department = models.CharField(max_length=100, primary_key=True, choices=DepartmentsList)

class Employees(models.Model):
    FullName = models.CharField(max_length=100)
    Role = models.CharField(max_length=100, choices=Role)
    Email = models.CharField(max_length=100, primary_key=True)
    Department=models.ForeignKey(Department, on_delete=models.CASCADE)


class Announcement(models.Model):

    Heading=models.CharField(max_length=100)
    Document=models.FileField(upload_to='documents/')
    DateRegistered=models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    FullName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, primary_key=True)
    Resident=models.CharField(max_length=100, choices=Resident)
    NationalId=models.CharField(max_length=10)
    License=models.FileField(upload_to='licenses/')
    RegisteredDate=models.DateTimeField(auto_now_add=True)




class Compensation(models.Model):

    CustomerID=models.ForeignKey(Customer, on_delete=models.CASCADE)
    DateRegistered=models.DateTimeField(auto_now_add=True)
    BankReceipt=models.FileField(upload_to='compensationReceipt/')



