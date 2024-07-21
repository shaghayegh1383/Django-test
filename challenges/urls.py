from django.urls import path
from . import views #از همین پوشه ایمپورت کن


urlpatterns = [
    path('sunday' , views.index),


    path ('Monday' , views.index)
]