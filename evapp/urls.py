from django.urls import path,include
from . import views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('customer/', include('django.contrib.auth.urls')),
    path('signup/',views.SignUpView,name='signup'),
]
