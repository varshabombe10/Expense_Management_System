from django.urls import path
from . import views 
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transaction/edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('transaction/delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('chart-data/', views.transaction_chart_data, name='transaction_chart_data'),
    path("profile/", profile, name="profile"),
    path('export_transactions/', export_transactions, name='export_transactions'),

]
