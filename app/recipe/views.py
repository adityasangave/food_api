from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import viewsets,generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from .serializers import TagSerializer


class TagViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)