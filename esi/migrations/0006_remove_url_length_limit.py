# Generated by Django 2.2.9 on 2020-04-14 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esi', '0005_remove_token_length_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbackredirect',
            name='url',
            field=models.TextField(default='/', help_text='The internal URL to redirect this callback towards.'),
        ),
    ]
