# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-06-26 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageflow', '0014_auto_20170626_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisresult',
            name='filter_name',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]
