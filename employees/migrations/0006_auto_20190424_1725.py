# Generated by Django 2.2 on 2019-04-24 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_auto_20190424_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='joining date',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='leaves',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='salary',
        ),
    ]
