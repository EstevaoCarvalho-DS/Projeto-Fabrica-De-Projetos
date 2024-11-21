from django.contrib import admin
from django.urls import path, include
from produtos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('produtos/', include('produtos.urls'))
]