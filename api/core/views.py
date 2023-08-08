from django.shortcuts import render
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework import viewsets

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
