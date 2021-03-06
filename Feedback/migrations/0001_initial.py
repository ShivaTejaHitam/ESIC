# Generated by Django 2.2.2 on 2020-02-22 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('email', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('password', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Minister',
            fields=[
                ('email', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('password', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(default='0', max_length=100, null=True)),
                ('ip_number', models.CharField(default='0', max_length=101, null=True)),
                ('Rating', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('sandf', models.CharField(default=None, max_length=50, null=True)),
                ('department', models.CharField(default=None, max_length=50, null=True)),
                ('AreaofIssue', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('Hygiene', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('DoctorBehaviour', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('WaitingTime', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('Pharmacy', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('Nurse', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('explanation', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('Status', models.CharField(blank=True, default='0', max_length=10, null=True)),
                ('otp', models.CharField(blank=True, default=None, max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(default='0', max_length=100)),
                ('ip_number', models.CharField(default='0', max_length=101)),
                ('Rating', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('sandf', models.CharField(default=None, max_length=50, null=True)),
                ('department', models.CharField(default=None, max_length=50, null=True)),
                ('AreaofIssue', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('AdmissionIssue', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('NurseIssue', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('DoctorIssue', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('AllotmentIssue', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('DischargeIssue', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('explanation', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('Status', models.CharField(blank=True, default='0', max_length=10, null=True)),
                ('otp', models.CharField(blank=True, default=None, max_length=6, null=True)),
            ],
        ),
    ]
