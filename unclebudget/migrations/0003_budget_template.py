# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unclebudget', '0002_auto_20170527_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='template',
            field=models.BooleanField(default=False),
        ),
    ]