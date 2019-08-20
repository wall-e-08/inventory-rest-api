from rest_framework import serializers
from .models import Warehouse
from v1_api.serializers import UserSerializer


class WarehouseSerializer(serializers.ModelSerializer):
    manager = UserSerializer(many=False)

    class Meta:
        model = Warehouse
        exclude = ['created',]
