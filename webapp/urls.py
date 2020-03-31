from django.urls import include, path

from . import views
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('social_django.urls')),
    path('profile/', views.profile),
    path('logout/', views.logout),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
