from django.contrib import admin
from .models import Task
# 2
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fiels = ('tasks',)
admin.site.register(Task, TaskAdmin)