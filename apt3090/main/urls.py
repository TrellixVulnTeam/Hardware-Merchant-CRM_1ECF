from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.landingpage),
    path("customer/<slug:username>/", views.customer, name='user'),
    path("intern/<slug:username>/", views.intern, name='intern'),
    path("products", views.products),
    path("supervisor", views.supervisor),
    path("create_order", views.createOrder, name='createorder'),

]