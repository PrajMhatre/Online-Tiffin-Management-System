# Generated by Django 3.2.8 on 2021-12-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorPortal', '0008_alter_vendor_customers_delivering'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_input', models.CharField(max_length=10)),
            ],
        ),
    ]
