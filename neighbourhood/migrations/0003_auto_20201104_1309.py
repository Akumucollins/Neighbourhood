# Generated by Django 3.1.2 on 2020-11-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0002_auto_20201104_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='hood_photo',
            field=models.ImageField(upload_to='hoods/'),
        ),
    ]
