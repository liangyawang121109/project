from django.urls import path
from . import views

urlpatterns = [
    path('memberadd/',views.memberadd),

]