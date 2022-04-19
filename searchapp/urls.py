from django.urls import path
from searchapp.views import index

urlpatterns = [
    path("", index, name="index")
]