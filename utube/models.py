from django.db import models
from django.utils import timezone

# Create your models here.
class video (models.Model):
	user = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	length = models.IntegerField()
	created_date = models.DateTimeField(
            default=timezone.now)

def publish(self):
        self.published_date = timezone.now()
        self.save()

def __str__(self):
	return self.title