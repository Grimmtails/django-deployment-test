from django.urls import path
from FifthLvlApp import views

app_name ='FifthLvlApp'
urlpatterns=[
    path('register',views.register,name='register'),
path('user_login/',views.user_login,name='user_login'),
]
