from rest_framework import viewsets
from .models import recipes
from .serializers import recipesSerializer

class recipesViewSet(viewsets.ModelViewSet):

    queryset = recipes.objects.all()
    serializer_class = recipesSerializer
