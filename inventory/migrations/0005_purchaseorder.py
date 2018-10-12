# Generated by Django 2.0.7 on 2018-09-30 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_holder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchaseorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('date_delivered', models.DateField()),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Section')),
            ],
        ),
    ]