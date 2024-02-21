# Generated by Django 1.11.20 on 2019-03-14 01:11

from django.conf import settings
from django.db import migrations, models
from django.db.backends.postgresql.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps


def set_users_for_existing_scheduledemails(
    apps: StateApps, schema_editor: DatabaseSchemaEditor
) -> None:
    ScheduledEmail = apps.get_model("zerver", "ScheduledEmail")
    for email in ScheduledEmail.objects.all():
        if email.user is not None:
            email.users.add(email.user)
        email.save()


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0210_stream_first_message_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="scheduledemail",
            name="users",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(
            set_users_for_existing_scheduledemails,
            reverse_code=migrations.RunPython.noop,
            elidable=True,
        ),
        migrations.RemoveField(
            model_name="scheduledemail",
            name="user",
        ),
    ]
