# Generated by Django 3.2.6 on 2021-10-18 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_remove_sale_positions'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Position',
        ),
    ]