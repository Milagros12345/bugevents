
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
                name='Promocion',
                fields=[
                    ('id',models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
                    ('nombre',models.CharField(max_length=50)),
                    ('porcentaje_descuento',models.FloatField()),
                    ('categoria',models.CharField(max_length=15)),
                    ('Paquete',models.ForeignKey(on_delete= django.db.models.deletion.CASCADE,to='inscripciones.Paquete')),
                ],
                options={
                'verbose_name_plural': 'Promociones',
            },
        ),
        
    ]
