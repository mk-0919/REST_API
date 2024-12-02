from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import recipesViewSet

router = DefaultRouter()
router.register('recipes', recipesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
