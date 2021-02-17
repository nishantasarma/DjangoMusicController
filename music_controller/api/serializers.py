from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        #id is primary key automatically created on every model in django
        fields = ('id', 'code', 'host','guest_can_pause','votes_to_skip', 'created_at')
