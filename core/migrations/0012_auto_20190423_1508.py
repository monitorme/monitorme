# Generated by Django 2.2 on 2019-04-23 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190422_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trackergroup',
            options={'permissions': (('can_edit_name', 'can edit name'), ('can_edit_avialable_to', 'can edit available to'), ('can_edit_active', 'can edit active'))},
        ),
        migrations.AlterModelOptions(
            name='trackergroupinstance',
            options={'permissions': (('can_edit_start', 'can edit start'), ('can_edit_end', 'can edit end'))},
        ),
    ]
