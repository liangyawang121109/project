from django.db import models

# Create your models here.

class scheduler_table(models.Model):
    contaner_name = models.CharField(max_length=200)
    environment_name = models.CharField(max_length=200)
    create_date = models.DateTimeField('date published')

    def __str__(self):
        return self.contaner_name
