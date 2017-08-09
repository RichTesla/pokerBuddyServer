# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 14:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20170809_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bets', to=settings.AUTH_USER_MODEL),
        ),
    ]
