# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 07:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_personalreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='proffesionalreview',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 7, 22, 7, 52, 47, 813207, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
