# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_code', models.PositiveIntegerField()),
                ('response_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField()),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
