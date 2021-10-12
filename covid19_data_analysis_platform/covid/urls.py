from django.urls import path
from covid import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'covid'

urlpatterns = [
    path('', views.index, name='index'),
    path('analysis/', views.analysis, name='analysis'),
    path('prediction/', views.prediction, name='prediction'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
