# Generated by Django 3.1.7 on 2021-05-28 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_auto_20210527_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.CreateModel(
            name='Watchlater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('watchlater_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relate_watchlater', to='auctions.listing')),
            ],
        ),
    ]
