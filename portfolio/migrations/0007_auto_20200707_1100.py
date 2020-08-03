# Generated by Django 3.0.7 on 2020-07-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_paintingdb_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paintingdb',
            name='series',
            field=models.CharField(choices=[('None', 'None'), ('Test Series', 'Test Series'), ('Test 2 Series', 'Test 2 Series')], default=1, max_length=100),
        ),
    ]