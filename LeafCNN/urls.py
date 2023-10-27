from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.Welcome),
    path('home.html',views.Welcome),
    path('contact.html',views.Contact),
    path('login.html',views.Login),
    path('signup.html',views.Signup),
    path('mainpage.html',views.Mainpage),
    path('result',views.Predictor,name='result'),



]
