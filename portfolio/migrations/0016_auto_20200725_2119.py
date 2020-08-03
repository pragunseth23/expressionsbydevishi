# Generated by Django 3.0.7 on 2020-07-26 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20200725_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='about',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='medium',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.series'),
        ),
    ]