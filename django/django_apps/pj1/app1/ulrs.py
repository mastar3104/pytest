from django.conf.urls import patterns, url
from app1 import views

urlpatterns = [
    url(r'^ipaddress/^$', views.index, name='ipaddress_list'),
]