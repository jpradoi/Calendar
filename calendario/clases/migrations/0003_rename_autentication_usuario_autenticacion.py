# Generated by Django 5.1.1 on 2024-09-08 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0002_alter_usuario_autentication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Autentication',
            new_name='Autenticacion',
        ),
    ]
