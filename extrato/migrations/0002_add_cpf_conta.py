# Generated by Django 4.2.3 on 2023-07-06 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('cpf', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cpf')),
            ],
        ),
    ]
