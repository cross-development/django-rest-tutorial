from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.snippet_list, name='snippet-list'),
    path('<int:pk>/', views.snippet_detail, name='snippet-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
