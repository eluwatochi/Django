from django.shortcuts import render
from rest_framework import generics
from .models import Artiste,Song
from .serializers import ArtisteSerializer,SongSerializer



# Create your views here.

class ArtisteList(generics.ListCreateAPIView):
    queryset= Artiste.objects.all()
    serializer_class= ArtisteSerializer

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Artiste.objects.all
    serializer_class= ArtisteSerializer

class SongList(generics.ListCreateAPIView):
    queryset= Song.objects.all()
    serializer_class= SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Song.objects.all()
    serializer_class= SongSerializer