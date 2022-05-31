from django.urls import path, include
from .views import TodoList, TodoById

urlpatterns = [
    path("todolist/",TodoList.as_view()),
    path("todolist/<str:pk>/",TodoById.as_view())
]
