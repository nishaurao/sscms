from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_list,name='user_list'),
    path('Add/', views.AddUser, name='AddUser'),
    path('Edit/<id>', views.EditUser,name='EditUser'),
    path('Delete/<id>', views.DeleteUser,name='DeleteUser'),
    path('View/<id>', views.ViewUser,name='ViewUser'),
]