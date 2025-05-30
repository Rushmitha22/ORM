# Generated by Django 5.2 on 2025-04-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('USER_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('USER_NAME', models.CharField(max_length=100)),
                ('PHONE_NUMBER', models.IntegerField()),
                ('EMAIL', models.EmailField(max_length=254)),
                ('MOVIE_NAME', models.CharField(max_length=100)),
                ('SEATS', models.IntegerField()),
            ],
        ),
    ]
