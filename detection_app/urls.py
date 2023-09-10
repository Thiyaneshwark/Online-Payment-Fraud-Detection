# detection_app/urls.py

from Capstone_project.urls import path
from . import views


urlpatterns = [
    path('',views.predictor,name='predictor'),
    path('result',views.forminfo, name='result')
]
