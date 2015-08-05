# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(serialize=False, primary_key=True)),
                ('short_link', models.CharField(max_length=16)),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]
