from django.urls import path, include
from .views import *

app_name = 'posts'

urlpatterns = [
    path('post/', PostAPIView.as_view()),
    path('list/', PostAPIView.as_view()),
    path('comment/', CommentAPIView.as_view()),
    path('post/', PostAPI_FBV), # 추가
    path('post/', PostAPIView2.as_view()),
]