from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.ViewAllTodo.as_view()),
    path('todo/<int:id>', views.ViewTodo.as_view()),
]
