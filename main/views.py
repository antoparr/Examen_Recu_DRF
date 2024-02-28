from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post,Valoracion
from .serializers import PostSerializer, ValoracionSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class ValoracionViewSet(viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def ordenar_fecha_registro(self, request):
        valoracion = Valoracion.objects.all().order_by('fecha_registro')
        serializer = ValoracionSerializer(valoracion, many=True, context={'request': request})
        return Response(serializer.data)
