# Generated by Django 3.2.4 on 2021-06-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_name_genre_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='title',
        ),
        migrations.AddField(
            model_name='genre',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
