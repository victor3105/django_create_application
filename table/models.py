from django.db import models


class TableField(models.Model):
    number = models.PositiveIntegerField(verbose_name='Порядковый номер')
    name = models.CharField(max_length=40, verbose_name='Имя')
    width = models.PositiveIntegerField(verbose_name='Ширина')
