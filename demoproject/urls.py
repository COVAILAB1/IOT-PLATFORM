from . import views
from django.urls import path

urlpatterns = [
    path('',views.testpage,name='page1')
]