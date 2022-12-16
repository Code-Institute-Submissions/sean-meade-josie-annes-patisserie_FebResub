# Generated by Django 4.1 on 2022-12-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_product_collection_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_size',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='large_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='medium_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]