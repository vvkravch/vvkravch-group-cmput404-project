# Generated by Django 2.1.7 on 2019-03-08 18:01

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190307_0042'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
    ]
