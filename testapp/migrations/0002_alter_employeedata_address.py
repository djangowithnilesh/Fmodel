# Generated by Django 4.1.3 on 2022-12-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]