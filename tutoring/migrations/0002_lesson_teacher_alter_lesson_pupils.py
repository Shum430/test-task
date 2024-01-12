# Generated by Django 5.0.1 on 2024-01-11 15:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutoring.teacher'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='pupils',
            field=models.ManyToManyField(related_name='lessons_as_pupil', to=settings.AUTH_USER_MODEL),
        ),
    ]