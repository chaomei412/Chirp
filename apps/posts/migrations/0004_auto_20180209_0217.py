# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import posts.model_validators


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180209_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='posts')),
            ],
        ),
        migrations.AlterField(
            model_name='postmedia',
            name='media',
            field=models.FileField(default=None, upload_to='posts', validators=[posts.model_validators.validate_file_extension_posts_media]),
        ),
    ]
