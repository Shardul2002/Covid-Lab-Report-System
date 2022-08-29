from django.db import models

# Create your models here.
class Patients(models.Model):
    FirstName=models.CharField(max_length=15)
    LastName=models.CharField(max_length=15)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=1)





class ReportField(models.Model):
    BloodPressure=models.CharField(max_length=10)
    OxygenLevel=models.IntegerField()
    Swaptype=models.CharField(max_length=15)
    measuredDateTime=models.DateTimeField(auto_now_add=True)
    STATUS=[('POSITIVE','Positive'),('NEGATIVE','Negative')]
    Status=models.CharField(choices=STATUS,max_length=10)
    patient=models.ForeignKey(Patients,on_delete=models.CASCADE)