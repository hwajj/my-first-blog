from django.urls import path
from . import views
from django.shortcuts import render, get_object_or_404

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

'''
views.post_detail라는 뷰를
post_detail이라 이름을 붙이도록 URL 법칙을 만듦
post_detail이라는 이름을 해석할 때,
blog/views.py파일 내부의 post_detail이라는 뷰 함수로 이해

브라우저에 http://127.0.0.1:8000/post/5/라고 입력하면,
장고는 post_detail 뷰를 찾아 매개변수 pk가 5인 값을 찾아 뷰로 전달
'''
