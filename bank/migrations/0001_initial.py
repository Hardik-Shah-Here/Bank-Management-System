# Generated by Django 3.2 on 2021-04-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=' ', max_length=50)),
                ('email', models.CharField(default=' ', max_length=50)),
                ('balance', models.IntegerField(default=0)),
                ('Date_of_Creation', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('T_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
