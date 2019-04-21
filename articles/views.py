from django.shortcuts import render
from rest_framework import viewsets
from .models import Articles
from .serializers import ArticlesSerializer

class ArticlesView(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer