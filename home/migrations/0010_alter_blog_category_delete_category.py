# Generated by Django 4.1.4 on 2023-09-02 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
