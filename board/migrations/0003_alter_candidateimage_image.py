# Generated by Django 5.1.3 on 2024-11-17 16:52

import board.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_candidateimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateimage',
            name='image',
            field=models.ImageField(upload_to='store/images', validators=[board.validators.vaidate_file_size]),
        ),
    ]