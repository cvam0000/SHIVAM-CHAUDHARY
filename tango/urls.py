from . import views
from django.urls import path


urlpatterns = [
    path('vishal',views.index,name='index'),
]
