# Generated by Django 2.2 on 2019-04-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0002_auto_20190410_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='short',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slice',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='sound',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='wrong',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
