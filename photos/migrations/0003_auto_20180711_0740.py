# Generated by Django 2.0.7 on 2018-07-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
