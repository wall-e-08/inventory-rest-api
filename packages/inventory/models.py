from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    whs_id = models.CharField(
        max_length=32,
        verbose_name="Warehouse Source ID"
    )
    capacity = models.IntegerField(verbose_name="Total capacity")
    remaining = models.IntegerField(verbose_name="Current amount")
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Model creation time")

    class Meta:
        ordering = ['created']

