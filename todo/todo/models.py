from django.db import models
from django.contrib.auth.models import User

class TODOO(models.Model):
    srno=models.AutoField(primary_key=True, auto_created=True)
    title=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


def __str__(self):
        return f"{self.title} - {self.user.username}"