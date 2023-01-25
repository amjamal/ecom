from django.urls import path
from . import views
app_name = 'ecom_project1app'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('allproducts/', views.allproducts, name='allproducts'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatDetail'),

]