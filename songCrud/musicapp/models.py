from django.db import models
from datetime import datetime


# Create your models here.

class Artiste (models.Model):
    first_name=models.CharField(max_length=400)
    last_name=models.CharField(max_length=400)
    age=models.IntegerField()


class Song(models.Model):
    artiste =models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title=models.CharField(max_length=40)
    date_released=models.DateField(default=datetime.today)
    likes=models.IntegerField()
    artisteId=models.IntegerField()


class Lyric(models.Model):
    Song =models.ForeignKey(Song, on_delete=models.CASCADE)
    content=models.CharField(max_length=40)
    song_id=models.IntegerField()

