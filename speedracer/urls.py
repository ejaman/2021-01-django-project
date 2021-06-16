from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name="login"),
    path('home/', views.home, name="home"),

    path('products/', views.products, name='products'),

    path('inventory/', views.list_item, name='inventory'),
    path('add/', views.create_item, name='add_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('search_basic/', views.search_basic, name='search_item'),
    path('search/', views.search, name = 'search_item2'),
    path('manager/<str:pk_test>/', views.manager, name="manager"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('viewbar', views.viewbar, name='viewbar'),
    path('viewpie', views.viewpie, name='viewpie'),
    path('graph3', views.graph3, name='graph3'),

]
