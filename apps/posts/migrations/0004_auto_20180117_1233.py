# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 12:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'Tags'},
        ),
    ]
