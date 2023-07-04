from django.urls import path
from catalog import views

urlpatterns = [
    path("" ,views.home, name="catalog"),
    path("catalog/product/<id>/view" ,views.view, name="product-view"),
    path("catalog/product/<id>/edit" ,views.edit, name="edit-product"),
]