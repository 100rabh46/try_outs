# Generated by Django 2.0.7 on 2019-04-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('stock_name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=100)),
                ('headquarters', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(max_length=100, null=True)),
                ('founded_on', models.CharField(max_length=100, null=True)),
                ('founders', models.CharField(max_length=100, null=True)),
                ('ceo', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
