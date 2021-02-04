from django.http import response
from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializer import RoomSerializer


class RoomView(generics.ListAPIView):
    query = Room.objects.all()
    serializer_class = RoomSerializer
    
    def get_queryset(self):
            pass    




