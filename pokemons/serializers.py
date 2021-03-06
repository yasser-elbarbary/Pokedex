from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    description = serializers.CharField()
    habitat = serializers.CharField(max_length=100)
    is_legendary = serializers.BooleanField(default=False)