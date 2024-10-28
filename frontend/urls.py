from django.urls import path
from . import views
app_name='frontend'


urlpatterns = [
   path('', views.home,name ='home'),
   path('create_item', views.create_item,name ='create_item'),
]
