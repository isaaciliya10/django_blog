# Generated by Django 4.2.3 on 2023-07-20 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_contact1_delete_contact_alter_emailus_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]