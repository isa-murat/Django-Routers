from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter




# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'last_name']
    search_fields = ['name', 'last_name']
    order_fields = ['name', 'last_name']


    @action(detail=False, methods=['get','post'])
    def address(self, request):
        return Response(data={"status":"OK",}, status=200)
