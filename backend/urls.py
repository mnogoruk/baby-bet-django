"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customers import views
from authentication.views import SomeApiView, CreateOrderView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/customers/', views.customers_list),
    path('api/customers/create', views.customer_create),
    path('api/customers/<int:pk>/', views.customers_detail),
    path('api-auth/', include('authentication.urls')),
    path('api/hello/', SomeApiView.as_view()),
    path('api/order/create', CreateOrderView.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
