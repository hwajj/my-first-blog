from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]


'''
views.post_detail라는 뷰를
post_detail이라 이름을 붙이도록 URL 법칙을 만듦
post_detail이라는 이름을 해석할 때,
blog/views.py파일 내부의 post_detail이라는 뷰 함수로 이해

브라우저에 http://127.0.0.1:8000/post/5/라고 입력하면,
장고는 post_detail 뷰를 찾아 매개변수 pk가 5인 값을 찾아 뷰로 전달
'''
