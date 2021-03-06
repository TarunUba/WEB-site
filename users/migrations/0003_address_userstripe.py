# Generated by Django 2.2.6 on 2019-12-06 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20191205_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStripe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.CharField(max_length=10)),
                ('house_no', models.CharField(max_length=120)),
                ('area', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('landmark', models.CharField(blank=True, max_length=120, null=True)),
                ('name', models.CharField(max_length=120)),
                ('mobile_no', models.CharField(max_length=10)),
                ('alternate_no', models.CharField(blank=True, max_length=10, null=True)),
                ('address_type', models.CharField(choices=[('H', 'Home Address'), ('W', 'Work/Office Address')], default='H', max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
