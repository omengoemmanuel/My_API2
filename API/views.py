from django.shortcuts import render
from .serializers import schoolserializer
from .models import school
from rest_framework import viewsets


# Create your views here.
class schoolview(viewsets.ModelViewSet):
    queryset = school.objects.all()
    serializer_class = schoolserializer
