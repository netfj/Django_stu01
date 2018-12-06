#coding:utf-8
# @Info: 
# @Author:Netfj@sina.com @File:urls.py.py @Time:2018/12/6 19:11

from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index')
]
