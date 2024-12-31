from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('done/<int:todo_id>', views.done, name="done"),
    path('delete/<int:todo_id>', views.delete, name="delete"),
]
