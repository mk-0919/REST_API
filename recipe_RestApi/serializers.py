from rest_framework import serializers
from .models import recipes

class recipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = recipes
        fields = ['id','title','making_time','serves','ingredients','cost']
