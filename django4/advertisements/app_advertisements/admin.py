from django.contrib import admin
from .models import Advertisement
# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','created_date','updated_date','auction']
    list_filter = ['auction']

admin.site.register(Advertisement,AdvertisementAdmin)