# Generated by Django 4.1.7 on 2023-05-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_curso_consultor_curso_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='consultor',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
