from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Valoracion


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ['url', 'id', 'titulo', 'cuerpo', 'user']


class ValoracionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Valoracion
        fields = ['url', 'id', 'rating', 'comment', 'fecha_registro', 'user', 'post']