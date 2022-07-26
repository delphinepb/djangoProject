# Generated by Django 4.0.1 on 2022-04-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('responsable', models.CharField(max_length=50)),
                ('statut_projet', models.CharField(max_length=50)),
                ('etat_avancement_projet', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('developpeur', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('duree_tache', models.CharField(max_length=20)),
                ('statut_tache', models.CharField(max_length=50)),
                ('etat_avancement_tache', models.CharField(max_length=20)),
            ],
        ),
    ]
