# Generated by Django 5.0 on 2023-12-28 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_service", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="job",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_service.user",
            ),
        ),
    ]
