from django.db import models


class Bridge(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    name = models.CharField(max_length=200, default="New Bridge")
    source_team = models.CharField(max_length=200)
    source_token = models.CharField(max_length=200)
    destination_team = models.CharField(max_length=200)
    destination_channel = models.CharField(max_length=200)
    destination_url = models.CharField(max_length=8000)

