# Generated by Django 3.2 on 2024-01-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prueba',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
