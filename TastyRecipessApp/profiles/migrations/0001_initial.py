# Generated by Django 4.2.11 on 2024-04-17 06:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(2, message='Nickname must be at least 2 chars long')])),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('chef', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
