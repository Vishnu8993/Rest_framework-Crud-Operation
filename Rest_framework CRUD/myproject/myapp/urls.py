from django.urls import path
from .views import PersonListCreateAPIView, PersonDetailAPIView

urlpatterns = [
    path('persons/', PersonListCreateAPIView.as_view(), name='person-list-create'),
    path('persons/<int:pk>/', PersonDetailAPIView.as_view(), name='person-detail'),
]
