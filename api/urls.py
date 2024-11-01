from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('user/', UserListCreateView.as_view(), name='user-list-create'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]
