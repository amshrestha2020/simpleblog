# Generated by Django 3.0.8 on 2020-07-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0003_auto_20200725_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='simpleblog.Category'),
        ),
    ]