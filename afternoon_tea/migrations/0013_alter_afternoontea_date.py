# Generated by Django 4.1 on 2022-12-12 20:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afternoon_tea', '0012_alter_afternoontea_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afternoontea',
            name='date',
            field=models.DateField(choices=[(datetime.date(2023, 1, 7), 'Sat: Jan 07'), (datetime.date(2023, 1, 8), 'Sun: Jan 08'), (datetime.date(2023, 1, 14), 'Sat: Jan 14'), (datetime.date(2023, 1, 15), 'Sun: Jan 15'), (datetime.date(2023, 1, 21), 'Sat: Jan 21'), (datetime.date(2023, 1, 22), 'Sun: Jan 22')]),
        ),
    ]
