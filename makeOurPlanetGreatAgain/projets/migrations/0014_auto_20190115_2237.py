# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-15 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0013_auto_20190115_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='commentaire',
            field=models.TextField(max_length=4000, verbose_name='Commentaire '),
        ),
    ]
