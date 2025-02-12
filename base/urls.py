from django.urls import path
from .views import TaskList, DetailView,TaskCreate

urlpatterns = [
    path("", TaskList.as_view(), name='home'),
    path('task/<int:pk>/',DetailView.as_view(), name='task'),
    path('task-create/',TaskCreate.as_view(), name='task-create'),
]
