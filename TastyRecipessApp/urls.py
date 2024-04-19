from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TastyRecipessApp.home.urls')),
    path('recipe/', include('TastyRecipessApp.recipes.urls')),
    path('profile/', include('TastyRecipessApp.profiles.urls')),
]
