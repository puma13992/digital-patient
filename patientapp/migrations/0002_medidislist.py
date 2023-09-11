# Generated by Django 3.2.20 on 2023-09-11 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediDisList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_or_disease_name', models.CharField(max_length=200, null=True)),
                ('instructions', models.CharField(blank=True, max_length=200, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.userprofile')),
            ],
        ),
    ]
