# Generated by Django 5.0.2 on 2024-02-21 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sscsmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
        ),
    ]
