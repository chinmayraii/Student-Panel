from django.db import models

class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=500,blank=True,null=True)
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=30)
    fees=models.IntegerField()
    duration=models.CharField(max_length=30)
    textfield=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.IntegerField()
    college=models.CharField(max_length=30)
    degree=models.CharField(max_length=30)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    total=models.IntegerField(default=0)
    paid=models.IntegerField(default=0)
    due=models.IntegerField(default=0)
    preserve_default=False
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name    

class Teacher(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.IntegerField()
    join=models.DateField()
    education=models.CharField(max_length=30)
    empid=models.IntegerField()
    exp=models.CharField(max_length=30)
    pack=models.CharField(max_length=30)
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name

