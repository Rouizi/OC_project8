# Generated by Django 2.2.6 on 2019-10-20 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20191020_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutri_score',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='substitute',
            name='nutri_score',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
