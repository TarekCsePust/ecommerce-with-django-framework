# Generated by Django 2.0.7 on 2018-08-28 06:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
    ]
