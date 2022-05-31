from django.shortcuts import render
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class TodoList(APIView):

    def get(self,request):
        todo = Todo.objects.all()
        serialize_data = TodoSerializer(todo,many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)


    def post(self,request):
        serialized_data = TodoSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.error,status=status.HTTP_400_BAD_REQUEST)




class TodoById(APIView):

    def get(self,request,pk):
        todo = Todo.objects.filter(id=pk)
        serialize_data = TodoSerializer(todo, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)


    def put(self,request,pk):
        todo = Todo.objects.filter(id=pk)
        todo.title = request.data.get("title")
        todo.desc = request.data.get("desc")
        serialize_data = TodoSerializer(todo, many=True)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.error,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        todo_obj = Todo.objects.filter(id=pk)
        todo_obj.delete()
        return Response({"status deleted"},status=status.HTTP_204_NO_CONTENT)

