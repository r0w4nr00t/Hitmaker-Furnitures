from django.urls import re_path, path
from .views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    re_path(r"^jwt/create/?", TokenObtainPairView.as_view(), name="jwt-create"),
    re_path(r"^jwt/refresh/?", TokenRefreshView.as_view(), name="jwt-refresh"),
    re_path(r"^jwt/verify/?", TokenVerifyView.as_view(), name="jwt-verify"),
]