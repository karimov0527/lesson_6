from django.urls import path
from .views import *

urlpatterns = [
    path('',smartphone),
    path('smartphone/<int:pk>',smartphone_det,name = 'smartphone_det')
]