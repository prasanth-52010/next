from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    #
    path('todo/', TodoListView.as_view(), name='todo-list'),

]
