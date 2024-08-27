from .models import school
from rest_framework import serializers


class schoolserializer(serializers.ModelSerializer):
    class Meta:
        model = school
        fields = '__all__'
