# Generated by Django 2.2.4 on 2019-09-17 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20190906_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveybase',
            name='survey_responsible_users',
        ),
    ]
