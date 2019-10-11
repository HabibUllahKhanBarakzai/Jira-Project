from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Project(TimeHistory):
    name = models.CharField(max_length=100)
    member = models.ManyToManyField("Member", related_name="projects")

    def __str__(self):
        return "{}".format(self.name)


class Member(AbstractUser):

    PROJECT_MANAGER = 1
    QUALITY_ASSURANCE = 2
    DEVELOPER = 3

    DESIGNATIONS = (
        (PROJECT_MANAGER, "PROJECT_MANAGER"),
        (QUALITY_ASSURANCE, "QUALITY_ASSURANCE"),
        (DEVELOPER, "DEVELOPER")
    )

    Designation = models.SmallIntegerField(choices=DESIGNATIONS, default=DEVELOPER)


class Subscription(TimeHistory):

    type = models.ForeignKey(to="Project", on_delete=models.CASCADE, related_name="subscription")
    number_of_allowed_members = models.SmallIntegerField(null=False)
    expiry_date = models.DateField(null=False)
