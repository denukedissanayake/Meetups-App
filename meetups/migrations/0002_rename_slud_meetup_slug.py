# Generated by Django 3.2.5 on 2021-07-09 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetup',
            old_name='slud',
            new_name='slug',
        ),
    ]
