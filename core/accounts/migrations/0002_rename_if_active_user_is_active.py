# Generated by Django 3.2.19 on 2023-06-05 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='if_active',
            new_name='is_active',
        ),
    ]