from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('brands/', views.brands, name='brands'),
#     path('cart/', views.cart, name='cart'),
#     path('checkout/', views.checkout, name='checkout'),
]