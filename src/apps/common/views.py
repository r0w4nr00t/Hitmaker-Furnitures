from rest_framework_simplejwt.views import (
    TokenRefreshView as TokenrefreshViewBase,
    TokenObtainPairView as TokenObtainPairViewBase,
    TokenVerifyView as TokenVerifyViewBase,
)

# Create your views here.
class TokenRefreshView(TokenObtainPairViewBase):
    ...
    
class TokenObtainPairView(TokenObtainPairViewBase):
    ...
class TokenVerifyView(TokenVerifyViewBase):
    ...