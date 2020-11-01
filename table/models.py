from django.db import models


class TableField(models.Model):
    number = models.PositiveIntegerField(verbose_name='Порядковый номер')
    name = models.CharField(max_length=40, verbose_name='Имя')
    width = models.PositiveIntegerField(verbose_name='Ширина')


class CSVPath(models.Model):
    path = models.FilePathField()

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.save()
