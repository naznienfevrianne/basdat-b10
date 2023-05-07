"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('authentication/', include('authentication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('manageteam/', include('manageteam.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
    path('peminjamanstadium/', include('peminjamanstadium.urls')),
    path('managepertandingan/', include('managepertandingan.urls'))
=======
    path('peminjamanstadium/', include('peminjamanstadium.urls'))
=======
    path('peminjamanstadium/', include('peminjamanstadium.urls')),
>>>>>>> 5edb2f40d9a7cdb72065bd8d7de86d7c6a4f290b
    path('list_pertandingan/', include('list_pertandingan.urls')),
    path('rapat/', include('rapat.urls'))
>>>>>>> 3599babf77ffed42b11e7ef96edc65b7b2078d8a
]
