# Generated by Django 1.11.20 on 2019-06-12 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0229_stream_message_retention_days"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userprofile",
            old_name="enable_stream_sounds",
            new_name="enable_stream_audible_notifications",
        ),
    ]
