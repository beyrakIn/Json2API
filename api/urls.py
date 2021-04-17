from django.urls import path
from .views import JSONFileView


urlpatterns = [
    path('jsonfile/<filename>/', JSONFileView.as_view()),

]
