# Generated by Django 1.11.28 on 2020-02-08 20:34
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0267_backfill_userpresence_realm_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userpresence",
            name="realm",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="zerver.Realm"),
        ),
        migrations.AlterIndexTogether(
            name="userpresence",
            index_together={("realm", "timestamp")},
        ),
    ]
