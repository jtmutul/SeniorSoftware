# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teamname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname_text', models.CharField(max_length=200)),
                ('category', models.ForeignKey(default='hello', on_delete=django.db.models.deletion.CASCADE, to='teams.Category')),
            ],
        ),
    ]
