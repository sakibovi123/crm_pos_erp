from django.urls import path, include
from Account import views

urlpatterns = [
    path("user-registration/", views.get_registration_page_for_user, name="UserRegistration"),
    # Url for login
    path("user-login/", views.get_login_for_user, name="UserLogin"),
]