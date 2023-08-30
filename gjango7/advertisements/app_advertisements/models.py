from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

# Create your models here.

User = get_user_model()
class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена',max_digits=10,decimal_places=2)
    auction = models.BooleanField('Торг',help_text='Отметьте если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,verbose_name='пользователь',on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')
    def __str__(self):
        return f"Advertisement(id={self.id}),title={self.title},price={self.price},auction={self.auction}"

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time= self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight:bold">Сегодня в {}</span>',created_time)
        else:
            return self.created_at.time().strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата последнего обновления')
    def updated_date(self):
        if self.updated_dt.date() == timezone.now().date():
            updated_time= self.updated_dt.time().strftime("%H:%M:%S")
            return format_html('<span style="color: blue; font-weight:bold">Сегодня в {}</span>',updated_time)
        else:
            return self.updated_dt.time().strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Фото')
    def image_small(self):
        if self.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px"/>',self.image.url)

    class Meta:
        db_table = "advertisements"