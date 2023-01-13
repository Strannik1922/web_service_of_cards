# Generated by Django 2.2.16 on 2023-01-12 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Menu_title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Item_title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Item_slug')),
                ('menu', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.Menu')),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='api.Item')),
            ],
            options={
                'verbose_name': 'Menu item',
                'verbose_name_plural': 'Menu items',
            },
        ),
    ]
