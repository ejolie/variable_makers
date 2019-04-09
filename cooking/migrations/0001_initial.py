# Generated by Django 2.2 on 2019-04-08 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kr_word', models.CharField(max_length=100, unique=True)),
                ('en_word', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('snake_case', models.TextField()),
                ('camel_case', models.TextField()),
                ('pascal_case', models.TextField()),
                ('copy_hits', models.IntegerField(default=0)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooking.Word')),
            ],
        ),
    ]
