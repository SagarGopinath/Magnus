# Generated by Django 5.0.6 on 2024-09-29 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_users_delete_feed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='message',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]