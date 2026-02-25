from django.contrib import admin
from .models import member

 

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joining_date",)
admin.site.register(member,MemberAdmin)