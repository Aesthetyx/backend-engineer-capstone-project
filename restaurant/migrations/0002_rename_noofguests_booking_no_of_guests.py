# Generated by Django 4.1.5 on 2023-01-16 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="noOfGuests",
            new_name="no_of_guests",
        ),
    ]
