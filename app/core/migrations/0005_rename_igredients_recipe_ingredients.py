# Generated by Django 3.2.14 on 2022-07-19 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220718_0722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='igredients',
            new_name='ingredients',
        ),
    ]
