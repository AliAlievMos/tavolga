# Generated by Django 4.0.8 on 2022-11-20 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_contacts_fb_alter_contacts_inst_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='mail',
        ),
    ]
