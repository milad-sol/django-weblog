# Generated by Django 4.2.19 on 2025-03-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/profile'),
        ),
    ]
