from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('loginn/', views.user_login, name='loginn'),
    path('todopage/', views.todo, name='todo'),

    path('delete_todo/<int:srno>/', views.delete_todo, name='delete_todo'),
    path('edit_todo/<int:srno>/', views.edit_todo, name='edit_todo'),

    path('signout/', views.signout, name='signout'),

    path('toggle/<int:srno>/', views.toggle_status, name='toggle_status'),

]
