# Generated by Django 3.1.13 on 2021-07-31 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('habitat', models.CharField(max_length=100)),
                ('is_legendary', models.BooleanField(default=False)),
            ],
        ),
    ]
