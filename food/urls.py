from django.urls import path
from food.views import *

app_name='s1'
urlpatterns=[
    path('biryani/',biryani,name='biryani'),
    path('chicken/',chicken,name='chicken'),
]