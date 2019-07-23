from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=10)
	description = models.TextField()
	opening_time = models.TimeField()
	#CharField(max_length=10)
	closing_time = models.TimeField()
	#CharField(max_length=10)


	def __str__(self):
		return self.name
