# Generated by Django 3.0.7 on 2020-07-07 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20200707_1102'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='paintingDB',
            new_name='artwork',
        ),
    ]