# Generated by Django 4.1.4 on 2023-09-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]
