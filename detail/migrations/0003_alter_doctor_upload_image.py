# Generated by Django 4.1.2 on 2022-11-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0002_doctor_patient_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='upload_image',
            field=models.ImageField(blank=True, upload_to='my_picture'),
        ),
    ]
