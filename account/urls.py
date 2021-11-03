from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #view de login
    #path('login/', views.user_login, name='login'),
    
    # urls para alteração de senha
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard')
]
    