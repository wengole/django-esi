# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esi', '0002_scopes_20161208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='access_token',
            field=models.CharField(editable=False, help_text='The access token granted by SSO.', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='refresh_token',
            field=models.CharField(blank=True, editable=False, help_text='A re-usable token to generate new access tokens upon expiry.', max_length=254, null=True),
        ),
    ]
