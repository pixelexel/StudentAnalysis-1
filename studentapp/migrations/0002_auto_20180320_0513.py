# Generated by Django 2.0.3 on 2018-03-19 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='no_of_siblingss',
            new_name='no_of_siblings',
        ),
    ]