from django.db import models


# Create your models here.

class school(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    admission_No = models.PositiveIntegerField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=10, null=False, blank=False, choices=gender_choices)
    date_of_birth = models.DateField()
    date_of_admission = models.DateField()
    photo = models.ImageField(upload_to='school/class', default='school/class/photo.jpg')

    def __str__(self):
        return self.name