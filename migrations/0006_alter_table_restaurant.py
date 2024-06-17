# Generated by Django 5.0.6 on 2024-06-17 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantManagement', '0012_delete_table'),
        ('TableManagement', '0005_remove_table_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='RestaurantManagement.restaurant'),
        ),
    ]