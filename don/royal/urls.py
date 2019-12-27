
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('list/',views.list,name="list"),
    path('delete/<int:id>/',views.employee_delete,name = 'employee_delete'),
    path('<int:id>/',views.index, name= 'employee_update')
    ]