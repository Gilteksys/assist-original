# Generated by Django 4.2.1 on 2023-05-22 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_cliente_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='documento',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='contato',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(max_length=50),
        ),
    ]
