from django.shortcuts import render
from .models import Box
from .serializers import mybox
from rest_framework import viewsets


class BoxViewSet(viewsets.ModelViewSet):
    queryset=Box.objects.all()
    serializer_class=mybox

