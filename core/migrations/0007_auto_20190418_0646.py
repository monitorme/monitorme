# Generated by Django 2.2 on 2019-04-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190417_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.IntegerField(),
        ),
    ]
