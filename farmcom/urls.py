"""
URL configuration for protfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from farmcom import views
app_name='farmcom'

urlpatterns = [
   path('about.html', views.about, name='about.html'),
   path('contact.html',views.contact, name='contact.html'),
   path('faq.html', views.faq, name='faq.html'),
   path('index_2.html', views.index_2, name='index_2.html'),
   path('index.html', views.index, name='index.html'),
   path('news_left_sidebar.html', views.news_left_sidebar, name='news_left_sidebar.html'),
   path('news_right_sidebar.html', views.news_right_sidebar, name='news_right_sidebar.html'),
   path('news_single.html', views.news_single, name='news_single.html'),
   path('pricing.html', views.pricing, name='pricing.html'),
   path('projects_single.html', views.projects_single, name='projects_single.html'),
   path('projects.html', views.projects, name='projects.html'),
   path('service_single.html', views.service_single, name='service_single.html'),

   path('services.html', views.services, name='services.html'),
   path('team.html', views.team, name='team.html'),
   path('testimonials.html', views.testimonials, name='testimonials.html'),
   path('typography.html', views.typography, name='typography.html'),


    path('info', views.info, name = 'info'),
        path('register', views.register, name = 'register'),
        path('login_reg', views.login_reg, name = 'login_reg'),
        path('logout', views.logoutuser, name = 'logout'),


        path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart'),

    ]