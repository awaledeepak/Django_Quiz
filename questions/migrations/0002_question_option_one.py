# Generated by Django 4.0.2 on 2022-02-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option_one',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
