# Generated by Django 2.2.2 on 2020-02-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0002_auto_20200222_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='hod',
            name='Name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='minister',
            name='Name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
