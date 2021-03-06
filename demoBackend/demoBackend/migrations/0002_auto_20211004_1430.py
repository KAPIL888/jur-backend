# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-10-04 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoBackend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academic',
            name='graduation',
        ),
        migrations.RemoveField(
            model_name='academic',
            name='post_graduation',
        ),
        migrations.RemoveField(
            model_name='academic',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='academic',
            name='school',
        ),
        migrations.RemoveField(
            model_name='college',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='school',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='Academic',
        ),
        migrations.DeleteModel(
            name='College',
        ),
        migrations.DeleteModel(
            name='School',
        ),
    ]
