# Generated by Django 2.2.4 on 2019-08-05 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agmp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='study_type',
            new_name='externalid_type',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='type_id',
            new_name='externalid_type',
        ),
    ]