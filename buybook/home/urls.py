from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='home'),
    path('product/<int:id>/',views.product,name='product'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
