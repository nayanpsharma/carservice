from django.contrib import admin
from django.urls import path
from servicing import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('servicing/<id>/', views.car_detail, name="car_detail"),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

