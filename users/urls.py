"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 登陆界面
    # 因为login要生成新的网页是直接蹦出来的（没有判断post/get，也不是返回到之前已有的
    # 网页，例如logout）所以视图参数为login而不是views.login
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),

    # 注销界面
    url(r'^logout/$', views.logout_view, name='logout'),

    # 注册界面
    url(r'^register/$', views.register, name='register'),


]

app_name = 'users'