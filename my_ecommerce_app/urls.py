# from django.urls import include, path
# from .views import add_to_cart, home, cart_view
# from my_ecommerce_app import views

# urlpatterns = [
#     path('', home, name='home'),
#     path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('category/<str:category>/', views.home, name='category'),
#     path('accounts/', include('accounts.urls')),
#     path('cart/', views.cart_view, name='cart'),
# ]


from django.urls import include, path
from .views import add_to_cart, add_to_cart_multiple, clear_cart, home, cart_view, payment

urlpatterns = [
    path('', home, name='home'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('category/<str:category>/', home, name='category'),
    path('accounts/', include('accounts.urls')),
    path('cart/', cart_view, name='cart'),
    path('payment/', payment, name='payment'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('add_to_cart_multiple/', add_to_cart_multiple, name='add_to_cart_multiple'),
]
