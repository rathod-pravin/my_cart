from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path("", views.index,name='ShopHome'),
    path("contact/", views.contact,name='Contact_Us'),
    path("about/", views.about,name='About_Us'),
    path("checkout/", views.checkout,name='Checkout'),
    path("tracker/", views.tracker,name='Track_Status'),
    path("prodview/", views.ProdView,name='Product_View'),
]
