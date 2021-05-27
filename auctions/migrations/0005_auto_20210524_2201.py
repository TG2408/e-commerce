# Generated by Django 3.1.7 on 2021-05-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210524_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='imagelink',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('All', 'All'), ('Fashion', 'Fashion'), ('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Books', 'Books')], default='All', max_length=100),
        ),
    ]
