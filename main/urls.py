from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ValoracionViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'valoracion', ValoracionViewSet, basename='valoracion')

urlpatterns = [
    path('', include(router.urls)),
]
