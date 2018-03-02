# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 01:46
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import posts.model_validators
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=500)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True,
                                                 related_name='liked', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True,
                                             on_delete=django.db.models.deletion.CASCADE, related_name='post_childs', to='posts.Post')),
                ('shared_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                  related_name='post_shared', to='posts.Post', verbose_name='If shared only')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=False, null=False, default=None, upload_to=posts.models.upload_posts_media_to,
                                           validators=[posts.model_validators.validate_file_extension_posts_media])),
                ('media_type', models.CharField(default='image', max_length=6)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='posts_media', to='posts.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostsMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
                ('impressions', models.IntegerField(default=0)),
                ('post', models.OneToOneField(blank=True,
                                              on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=140)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
