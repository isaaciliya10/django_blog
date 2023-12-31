# Generated by Django 4.2.1 on 2023-07-17 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_alter_emailus_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Conatcts',
            },
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AlterField(
            model_name='emailus',
            name='email',
            field=models.EmailField(max_length=225),
        ),
    ]
