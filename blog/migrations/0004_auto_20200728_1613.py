# Generated by Django 2.0.3 on 2020-07-28 08:13

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(verbose_name='文章详情'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
