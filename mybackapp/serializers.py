from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']



class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"
