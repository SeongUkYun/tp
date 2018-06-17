from django.db import models


class Order(models.Model):
    number = models.CharField('受注番号', max_length=8, null=True)
    order_date = models.DateField('受注日', null=False)
    code = models.CharField('コード', max_length=8, null=False)
