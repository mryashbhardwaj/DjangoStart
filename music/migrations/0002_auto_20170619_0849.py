# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Songs',
            new_name='Song',
        ),
    ]
