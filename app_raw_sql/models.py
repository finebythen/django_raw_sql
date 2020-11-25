from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(default=0)
    user_created = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
