# Generated by Django 3.2.8 on 2021-10-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Careated At')),
            ],
        ),
    ]
