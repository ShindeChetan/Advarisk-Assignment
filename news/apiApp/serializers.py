from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Article, SearchTable


class UserSerializer(serializers.ModelSerializer):
    """User model serializer class used to validate and
       serialize user data

    Args:
        serializers: Model serializer
    """    
    class Meta:       
        model=get_user_model()
        fields=["username", "email", "password","is_banned"]
        extra_kwargs={
            "password":{
                "style": {'input_type':'password'},
                "write_only":True,
                "min_length":5,
            },
            "is_banned":{
                "read_only":True,
            }
            
        }
    def create(self, validate_data):
        """Cretes the user

        Args:
            validate_data (dict): validated data

        Returns:
            user: instance of created user
        """        
        user_model = get_user_model()
        password=validate_data.pop("password")
        user=user_model.objects.create(**validate_data)
        user.set_password(password)
        user.save()
        return user
        

class LoginSerializer(serializers.Serializer):
    """Login Serializer

    Args:
        serializers (Serializer): django Serializer
    """    
    username=serializers.CharField()
    password=serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False, # django trims whitespace from charfields by default.
    )
    
    def validate(self, attrs):
        """ validated the data

        Args:
            attrs (dict): python dictionary for validation

        Raises:
            serializers.ValidationError

        Returns:
            dict : dictionary of validated data
        """        
        user=authenticate(
            username=attrs.get('username'),
            password=attrs.get('password'),
        )
        if not user:
            msg=('Unable to authenticate the user with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')
        
        attrs['user']=user
        return attrs
        
"""Search Serializer
"""
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=SearchTable
        fields="__all__"

"""Article Serializer
"""
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields="__all__"

""" News Serializer
"""
class NewsSerializer(serializers.Serializer):
    keyword=serializers.CharField(required=True, allow_blank=False)
    