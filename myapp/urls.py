from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.User_login, name='login'),
    path('signup/', views.User_signup, name='signup'),
    path('homepage/', views.index, name='homepage'),
    path('logout/', views.user_logout, name='logout'),
    
]
