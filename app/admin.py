from django.contrib import admin
from .models import Parent, Teacher, Group, Child, Attendance

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "email")
    search_fields = ("first_name", "last_name", "phone", "email")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "email")
    search_fields = ("first_name", "last_name", "phone", "email")

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher")
    search_fields = ("name",)

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date", "group")
    search_fields = ("first_name", "last_name")
    list_filter = ("group",)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("child", "date", "present")
    search_fields = ("child__first_name", "child__last_name", "date")
    list_filter = ("date", "present")
