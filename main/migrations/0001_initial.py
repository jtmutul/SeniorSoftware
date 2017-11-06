# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 06:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScoringCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteriaName', models.CharField(max_length=100)),
                ('score', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=200)),
                ('score', models.IntegerField()),
                ('category', models.ManyToManyField(to='main.Category')),
                ('member', models.ManyToManyField(blank=True, to='main.Member')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='criteria',
            field=models.ManyToManyField(blank=True, to='main.ScoringCriteria'),
        ),
    ]
