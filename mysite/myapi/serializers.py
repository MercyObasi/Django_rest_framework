from re import search
from rest_framework import serializers
from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('pk','name', 'alias')  # '__all__'  