# Generated by Django 4.2.3 on 2023-07-18 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_customuser_auth_age_alter_customuser_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
