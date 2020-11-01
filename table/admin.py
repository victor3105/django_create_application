from django.contrib import admin
from .models import TableField, CSVPath


@admin.register(TableField)
class TableFieldAdmin(admin.ModelAdmin):
    pass


@admin.register(CSVPath)
class CSVPathAdmin(admin.ModelAdmin):
    pass
