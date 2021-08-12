
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('reg', views.reg, name='reg'),
    path('anti', views.anti, name='anti'),
    path('service', views.service, name='service'),
    path('uslugi', views.uslugi, name='uslugi'),
    path('uslug1', views.uslug1, name='uslug1'),
    path('uslug2', views.uslug2, name='uslug2'),
    path('uslug3', views.uslug3, name='uslug3'),
    path('uslug4', views.uslug4, name='uslug4'),
    path('uslug5', views.uslug5, name='uslug5'),
    path('index', views.index, name='index'),
    path('otdel', views.otdel, name='otdel'),
    path('voprose', views.voprose, name='voprose'),

]
