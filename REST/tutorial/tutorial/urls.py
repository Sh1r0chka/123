from django.contrib import admin
from django.urls import include, path # Добавляем include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
]
