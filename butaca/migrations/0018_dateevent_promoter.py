# Generated by Django 4.2.3 on 2023-07-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('butaca', '0017_dateevent_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateevent',
            name='promoter',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
