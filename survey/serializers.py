from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    class Meta:
        model = User
        fields = ('username', 'password', 'email')