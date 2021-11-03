# Generated by Django 3.2.8 on 2021-10-11 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('RG', models.CharField(max_length=14)),
                ('CPF', models.CharField(max_length=14)),
                ('DataCadastro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('DataNascimento', models.DateTimeField(blank=True)),
            ],
        ),
    ]
