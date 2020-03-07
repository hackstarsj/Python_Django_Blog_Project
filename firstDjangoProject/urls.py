"""firstDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from firstDjangoProject import settings
from firstapp import urls
from django.conf.urls import include, url
from firstapp import views

urlpatterns = [
    # url(r'^hello/', 'firstapp.views.hello', name='hello'),
    url(r'^$', views.hello, name='home'),
    url(r'datashow/$', views.showAllData, name='showdata'),
    path('addData',views.AddData,name="adddata"),
    path('submit_form', views.SaveData, name="submit_form"),
    path('update_data',views.UpdateData,name='update_data'),
    path('delete_data/<str:post_id>', views.DeleteData,name="deletedata"),
    path(r'datasingle/<str:link_url>', views.showSinglPost, name='showsingle'),
    path('register_user',views.RegisterUsers,name="register_user"),
    path('register_user/<str:error_data>', views.RegisterUsersData, name="register_user_data"),
    path('save_user', views.Save_user, name="save_user"),
    #path('login', views.Login, name="login"),
    path('login/', views.Login, name="login"),
    path('login_user', views.LoginRequest, name="login_user"),
    path('user_home', views.User_home, name="user_home"),
    path('logout', views.LogOut, name="user_home"),
    path('admin/', admin.site.urls),
    path('chat/', include('firstapp.urls')),
    path('template_example_1/', views.template_example_1,name="template_example_1"),
    path('template_example_2/', views.template_example_2, name="template_example_2"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
