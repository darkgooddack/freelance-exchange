# Generated by Django 5.1.5 on 2025-01-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='description',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='decs',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='description',
            new_name='desc',
        ),
        migrations.AddField(
            model_name='ticket',
            name='desc',
            field=models.CharField(default='default_value', max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('1', 'Веб разработка'), ('2', 'Маркетинг'), ('3', 'Копирайтинг'), ('4', 'Рерайтиинг'), ('5', 'Переводы'), ('6', 'Видеомонтаж'), ('7', 'Фотография')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[('1', 'Веб разработка'), ('2', 'Маркетинг'), ('3', 'Копирайтинг'), ('4', 'Рерайтиинг'), ('5', 'Переводы'), ('6', 'Видеомонтаж'), ('7', 'Фотография')], default='1', max_length=1),
        ),
    ]
