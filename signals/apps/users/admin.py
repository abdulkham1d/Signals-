from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    pass
