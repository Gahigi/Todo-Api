from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

# Create your views here.
class ViewAllTodo(APIView):
    def get(self, request):
        todo = Todo.objects.all()
        serializers_data = TodoSerializer(todo, many= True)
        return Response(serializers_data.data, status= status.HTTP_200_OK)
    def put(self, request):
        serializers_data = TodoSerializer(data=request.data)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response(serializers_data.data, status= status.HTTP_201_CREATED)
        return Response(serializers_data.errors, status= status.HTTP_400_BAD_REQUEST)
class ViewTodo(APIView):
    def get(self, request, id):
        todo = Todo.objects.get(id = id)
        serializers_data = TodoSerializer(todo)
        return Response(serializers_data.data, status= status.HTTP_200_OK)
    def put(self, request, id):
        todo = Todo.objects.get(id = id)
        serializers_data = TodoSerializer(todo, data= request.data)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response(serializers_data.data, status= status.HTTP_201_CREATED)
        return Response(serializers_data.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        todo = Todo.objects.get(id = id)
        todo.delete()
        return Response({"Status": "Deleted"})    