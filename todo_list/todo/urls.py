from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('app', views.app, name='app'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]
