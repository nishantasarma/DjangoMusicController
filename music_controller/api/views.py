from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
# Create your views here.

#ListAPIView doesnot give the post form
#CreateApiView give sthe post form
class RoomView(generics.CreateAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
