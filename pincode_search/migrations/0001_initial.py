# Generated by Django 4.1.7 on 2023-04-22 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PincodeMealMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(max_length=6)),
                ('meal_options', models.CharField(max_length=200)),
            ],
        ),
    ]
