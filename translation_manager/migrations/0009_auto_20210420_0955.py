# Generated by Django 3.2 on 2021-04-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation_manager', '0008_auto_20200120_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remotetranslationentry',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='translationbackup',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='translationentry',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]