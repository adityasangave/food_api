from urllib import request
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import viewsets,generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe, Tag, Ingredient
from .serializers import *


class RecipeAttrViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TagViewSet(RecipeAttrViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class IngredientViewSet(RecipeAttrViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    def get_queryset(self):
        return self.queryset.filter(user=request.user)


    def get_serializer_class(self):
        if self.action == "retrieve":
            return RecipeDetailSerializer
        
        return RecipeSerializer