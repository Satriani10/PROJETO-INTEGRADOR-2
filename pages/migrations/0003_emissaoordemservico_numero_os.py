# Generated by Django 5.1.1 on 2024-10-09 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_ordemservico'),
    ]

    operations = [
        migrations.AddField(
            model_name='emissaoordemservico',
            name='numero_os',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
