# Generated by Django 5.0.12 on 2025-02-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='categorias/', verbose_name='Imagen de categoría'),
        ),
    ]
