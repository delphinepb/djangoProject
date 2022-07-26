# Generated by Django 4.0.1 on 2022-04-12 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_projet_taches'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developpeur',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_developpeur', models.CharField(max_length=50)),
                ('prénom_developpeur', models.CharField(max_length=50)),
                ('taches_developpeur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_responsable', models.CharField(max_length=50)),
                ('prénom_responsable', models.CharField(max_length=50)),
                ('projets_responsable', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='projet',
            name='responsable',
        ),
        migrations.RemoveField(
            model_name='tache',
            name='developpeur',
        ),
        migrations.CreateModel(
            name='Relation_Tache_Developpeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_developpeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.developpeur')),
                ('id_tache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.tache')),
            ],
        ),
        migrations.CreateModel(
            name='Relation_Projet_Responsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.projet')),
                ('id_responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.responsable')),
            ],
        ),
        migrations.AddField(
            model_name='projet',
            name='responsable',
            field=models.ManyToManyField(through='App.Relation_Projet_Responsable', to='App.Responsable'),
        ),
        migrations.AddField(
            model_name='tache',
            name='developpeur',
            field=models.ManyToManyField(through='App.Relation_Tache_Developpeur', to='App.Developpeur'),
        ),
    ]
