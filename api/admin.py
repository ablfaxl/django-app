from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    search_fields = ('name', 'age')
    ordering = ('id',)
    list_per_page = 10

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.order_by('id')
        return queryset
