from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)

admin.site.register(Lead, LeadAdmin)
