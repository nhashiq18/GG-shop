# Generated by Django 4.1.4 on 2023-01-02 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_log_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="log",
            old_name="profile",
            new_name="user",
        ),
    ]