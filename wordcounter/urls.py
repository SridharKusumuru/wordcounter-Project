from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage , name = 'home'),
    path('submits/', views.submit_one, name = 'submit_one'),
    path('about_info/' , views.about_info, name = 'about_info'),  
]
