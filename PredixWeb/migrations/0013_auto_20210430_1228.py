# Generated by Django 3.1.7 on 2021-04-30 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PredixWeb', '0012_movies_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='rating',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
