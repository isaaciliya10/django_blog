# Generated by Django 4.2.3 on 2023-07-08 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_category_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.category'),
            preserve_default=False,
        ),
    ]
