from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('estate_app/', include('estate_app.urls')),
    path('admin/', admin.site.urls),
]
