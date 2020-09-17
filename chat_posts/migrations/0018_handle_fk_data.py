# Generated by Django 3.0.8 on 2020-09-17 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_posts', '0017_add_handle_fk'),
    ]

    operations = [
        migrations.RunSQL([
            (
                "UPDATE chat_posts_posts "
                "JOIN chat_posts_handles "
                "ON chat_posts_posts.handleName = chat_posts_handles.name "
                "SET chat_posts_posts.handle_id = chat_posts_handles.id;"
            ),
        ])
    ]
