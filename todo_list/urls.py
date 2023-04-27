from django.contrib import admin
from django.urls import path
from todo_list import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.about, name='about'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('crossoff/<item_id>', views.cross_off, name='cross_off'),
    path('uncross/<item_id>', views.uncross, name='uncross'),
    path('edit/<item_id>', views.edit, name='edit'),
    path('signup/', views.signup, name='signup'),
]
