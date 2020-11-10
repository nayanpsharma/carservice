from django.contrib import admin

from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_model', 'car_notes', 'car_number', 'year_old', 'service_type']
