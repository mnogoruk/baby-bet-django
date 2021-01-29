from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authentication.views import CustomUserCreate, MyTokenObtainPairView, MyTokenRefreshView, \
    LogoutAndBlacklistRefreshTokenForUserView

urlpatterns = [
    path('user/create', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain', MyTokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist')
]