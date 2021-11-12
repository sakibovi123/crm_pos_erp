from django.db import models

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to="images/", null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.first_name)

    def get_username(username):
        try:
            UserModel.objects.get(username=username)
        except:
            return False

