from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addtask, name='addtask'),
    path('mark_done/<int:pk>/', views.mark_done, name='mark_done'),
    path('mark_undone/<int:pk>/', views.mark_undone, name='mark_undone'),
    path('update/<int:pk>/', views.update, name='update'),
    path('del/<int:pk>/', views.delete, name='delete'),
]