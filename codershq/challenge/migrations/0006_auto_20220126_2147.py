# Generated by Django 3.2.11 on 2022-01-26 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenge', '0005_auto_20220126_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Challenge end date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challenge',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
    ]
