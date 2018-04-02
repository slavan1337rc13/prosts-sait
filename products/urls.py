from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.products_list, name='products_list'),

]