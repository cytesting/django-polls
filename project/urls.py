from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req: redirect('/polls/')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
