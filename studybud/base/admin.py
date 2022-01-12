from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Room)
admin.site.register(models.Topic)
admin.site.register(models.Message)


# class RoomAdmin(admin.ModelAdmin):
#     list_display = ('name')
