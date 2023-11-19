from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Member)

class  MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'joined_date')

admin.site.register(models.Member, MemberAdmin)