from django.db import models

# Create your models here.
class Department(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    dept_location=models.CharField(max_length=100)

class Employee(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    emp_job=models.CharField(max_length=100)
    mgr_no=models.IntegerField()
    hiredate=models.DateField()
    salary=models.IntegerField()
    comm=models.IntegerField()
    dname=models.ForeignKey(Department,on_delete=models.CASCADE)
