from django.db import models

from users.models import CustomUser


class Transports(models.Model):
    """Модель Транспорты"""
    TRANSPORT_TYPES = [
        ('C', 'Car'),
        ('B', 'Bike'),
        ('S', 'Scooter')
    ]
    can_be_rented = models.BooleanField(default=False, verbose_name='Можно ли арендовать транспорт?')
    transport_type = models.CharField(max_length=10, choices=TRANSPORT_TYPES, verbose_name='Тип транспорта')
    model = models.CharField(max_length=100, verbose_name='Модель транспорта')
    color = models.CharField(max_length=50, verbose_name='Цвет транспорта')
    identifier = models.CharField(max_length=20, verbose_name='Номерной знак')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    latitude = models.DecimalField(default=0, max_digits=9, decimal_places=6,
                                   verbose_name='Географическая широта местонахождения транспорта')
    longitude = models.DecimalField(default=0, max_digits=9, decimal_places=6,
                                    verbose_name='Географическая долгота местонахождения транспорта')
    minute_price = models.FloatField(default=0, blank=True, null=True, verbose_name='Цена аренды за минуту')
    day_price = models.FloatField(default=0, blank=True, null=True, verbose_name='Цена аренды за сутки')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Хозяин транспорта')

    def __str__(self):
        return f'{self.model} - {self.color}'
