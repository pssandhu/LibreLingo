# Generated by Django 3.0.3 on 2020-03-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_auto_20200302_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='special_characters',
            field=models.TextField(default='', verbose_name='Space-separated list of haracters for the virtual keyboard'),
            preserve_default=False,
        ),
    ]
