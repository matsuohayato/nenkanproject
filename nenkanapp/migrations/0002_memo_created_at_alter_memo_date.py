# Generated by Django 4.0 on 2025-02-26 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nenkanapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memo',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]
