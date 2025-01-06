# health_analysis/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('breakeven.urls')),  # Include breakeven app URLs
]
