# Generated by Django 5.0.6 on 2024-06-12 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TableManagement', '0002_remove_table_reservation_remove_table_table_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RestaurantLogin',
        ),
    ]