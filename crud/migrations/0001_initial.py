# Generated by Django 3.1.7 on 2021-04-01 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosGrales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('folio', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=35)),
                ('confirma', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=12)),
                ('domicilio', models.CharField(max_length=50)),
                ('alcaldia', models.CharField(max_length=50)),
                ('mascota', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=30)),
                ('peso', models.IntegerField()),
                ('tiposervicio', models.CharField(max_length=20)),
                ('fechaingreso', models.DateField()),
                ('horario', models.CharField(max_length=10)),
                ('puntual', models.CharField(max_length=10)),
                ('mensajero', models.CharField(max_length=10)),
                ('quiencrema', models.CharField(max_length=10)),
                ('entregaurna', models.CharField(max_length=10)),
                ('quienentrega', models.CharField(max_length=10)),
                ('procedencia1', models.CharField(max_length=10)),
                ('procedencia2', models.CharField(max_length=10)),
                ('pago', models.IntegerField()),
                ('formapago', models.CharField(max_length=15)),
                ('servicios', models.CharField(max_length=5)),
                ('tamaño', models.CharField(max_length=5)),
                ('tipo', models.CharField(max_length=10)),
                ('mvzrecomienda', models.CharField(max_length=25)),
                ('comision', models.IntegerField()),
                ('eutanasia', models.IntegerField()),
                ('tipourna', models.CharField(max_length=20)),
                ('importadas', models.CharField(max_length=20)),
                ('huellas', models.CharField(max_length=20)),
                ('otros', models.CharField(max_length=25)),
                ('condiciones', models.CharField(max_length=15)),
                ('fechadeceso', models.DateField()),
                ('observaciones', models.TextField(max_length=100)),
                ('capturo', models.CharField(max_length=15)),
            ],
        ),
    ]
