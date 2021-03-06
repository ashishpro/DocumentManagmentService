# Generated by Django 3.2.11 on 2022-01-16 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0005_auto_20220116_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='document_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
