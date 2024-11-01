from rest_framework import generics, status
from rest_framework.response import Response

from .message import user_message
from .models import User
from .serializer import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {"data": serializer.data, "message": user_message['201']},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"error_message": f"Invalid data: {serializer.errors} {user_message['400']}"},
            status=status.HTTP_400_BAD_REQUEST
        )


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                {"data": serializer.data, "message": user_message['201']},
                status=status.HTTP_200_OK
            )
        return Response(
            {"error_message": f"{serializer.errors}, {user_message['400']}"},
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": user_message['200']},
            status=status.HTTP_200_OK
        )
