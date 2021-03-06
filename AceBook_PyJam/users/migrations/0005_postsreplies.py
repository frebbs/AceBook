# Generated by Django 2.2.10 on 2020-02-11 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20200210_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostsReplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_content', models.CharField(max_length=10000)),
                ('reply_created', models.DateTimeField(auto_now_add=True)),
                ('reply_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
