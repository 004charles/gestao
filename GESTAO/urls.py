
from django.contrib import admin
from django.urls import path,include
from gestaoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestaoapp/', include('gestaoapp.urls')),
    path('', views.index, name='index'),
]
