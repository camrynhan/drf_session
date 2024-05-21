from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

# 기본 serializer
class PostBaseSerializer(serializers.Serializer):
    image = serializers.ImageField(required=False)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    view_count = serializers.IntegerField()
    writer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    bad_post = serializers.BooleanField()

# create 추가
    def create(self, validated_data):
        writer_id = validated_data['writer'] #validated_data에서 writer 필드로부터 사용자 ID 가져옴
        writer_instance = User.objects.get(id=writer_id)
        #해당 ID를 가진 사용자의 인스턴스를 가져옴.

        post = Post.objects.creat(
            content=validated_data['content'],
            view_count=validated_data['view_count'],
            writer=writer_instance, #가져온 사용자 인스턴스를 writer필드에 할당
        )
        return post
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'