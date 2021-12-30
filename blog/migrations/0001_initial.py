# Generated by Django 4.0 on 2021-12-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_post', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=360)),
            ],
        ),
    ]