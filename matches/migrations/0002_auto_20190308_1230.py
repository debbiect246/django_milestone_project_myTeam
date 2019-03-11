# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-08 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0002_auto_20190308_1230'),
        ('profile_and_stats', '0001_initial'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playermatchavailability',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_and_stats.UserProfileData'),
        ),
        migrations.AddField(
            model_name='matchdata',
            name='associated_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group'),
        ),
        migrations.AddField(
            model_name='matchdata',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to='profile_and_stats.UserProfileData'),
        ),
        migrations.AddField(
            model_name='matchdata',
            name='players',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='profile_and_stats.UserProfileData'),
        ),
    ]