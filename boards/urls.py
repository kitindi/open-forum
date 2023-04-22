from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home/board/<str:pk>', views.board_topics, name='board-topics'),
    path('home/board/<str:pk>/create/', views.create_topic, name='create-topics'),
    
]
