# Generated by Django 3.1.4 on 2020-12-05 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default='2000-01-01', verbose_name='Дата рождения'),
        ),
    ]
