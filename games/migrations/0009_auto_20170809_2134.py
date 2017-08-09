# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 21:34
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_auto_20170809_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='result',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
