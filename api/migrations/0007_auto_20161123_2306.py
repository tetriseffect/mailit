# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 23:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20161123_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailitem',
            old_name='senderFirstName',
            new_name='senderName',
        ),
        migrations.RemoveField(
            model_name='mailitem',
            name='senderLastName',
        ),
    ]
