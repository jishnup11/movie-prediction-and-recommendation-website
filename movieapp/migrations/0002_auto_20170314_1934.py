# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userid',
            field=models.IntegerField(default=0),
        ),
    ]