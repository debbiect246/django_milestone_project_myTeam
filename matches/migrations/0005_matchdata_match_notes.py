# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-09 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_auto_20190308_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchdata',
            name='match_notes',
            field=models.TextField(blank=True, max_length='200', null=True),
        ),
    ]
