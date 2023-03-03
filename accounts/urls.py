from django.urls import path
from .views import *
from accounts import *


urlpatterns = [
    path('', Home, name='home'),
    #path('login', login_user, name='login')
    path('register/', UserRegisterView.as_view(), name='register'),
    path('password/', PasswordsChangeView.as_view(template_name="registration/change-password.html")),
    path('edit-user/', UserChangeForm.as_view(template_name='registration/user_edit_form.html')),
]
