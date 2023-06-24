from django.urls import include, path
from accounts.api.v1 import views

app_name = 'api-v1'

urlpatterns = [
    path('', views.ProfileApiView.as_view(), name='profile'),

]