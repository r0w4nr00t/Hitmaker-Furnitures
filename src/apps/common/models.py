from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import UserManager as BaseUserManager
from django.utils import timezone
# from .utils.mail import send_mail


class UserManager(BaseUserManager):
    def create_user(self,email, password =None, role=None, **extra_fields):
        if not role:
            raise ValueError("The user role must be set")
        """
        Creates and saves a User with the given email and
        password.
        """
        now = timezone.now()
        if not email:
            raise ValueError("The given email must be set")
        email = UserManager.normalize_email(email)
        user = self.model(
            email=email,
            role=role,
            username=email,
            is_staff=False,
            is_active=True,
            is_superuser=False,
            last_login=now,
            date_joined=now,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email, password, role="Admin", **extra_fields):
        user = self.create_user(email, password, role=role **extra_fields)
        user.is_staff= True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    ...


class User(AbstractUser):
    # AuthProvider = models.TextChoices('AuthProviders', 'EMAIL_AND_PASSWORD GOOGLE')
    Role = models.TextChoices('Roles', 'ADMIN CUSTOMER')
    email = models.EmailField(
        verbose_name= "email address",
        max_length= 255,
        unique=True,
    )
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_staff = models.BooleanField(
        default=False,
        help_text=("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        default=True,
        help_text=(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    # auth_provider = models.CharField(choices=AuthProvider.choices, max_length=18, default=AuthProvider.EMAIL_AND_PASSWORD)
    picture = models.URLField()
    role = models.CharField(max_length=8, choices=Role.choices)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['role']
    
    objects= UserManager()
    
    class Meta:
        # abstract =True
        get_latest_by = "date_joined" 

    # def email_user(self, subject, message, from_email = None, **kwargs):
    #     """ 
    #     Send an email to this user
    #     """
    #     return send_mail()
    
class CreatedUpdatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)