# Generated by Django 3.1.7 on 2021-04-17 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PredixWeb', '0004_auto_20210417_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='mname',
        ),
    ]
