# Generated by Django 2.2.5 on 2021-07-26 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Artist', models.CharField(max_length=30)),
                ('Genre', models.CharField(max_length=50)),
            ],
        ),
    ]
