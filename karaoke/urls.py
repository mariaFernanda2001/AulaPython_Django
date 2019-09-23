from django.urls import path
from . import views

urlpatterns = [
    # AS aspas corresponde o localHost
    path('', views.index, name='Index')
]