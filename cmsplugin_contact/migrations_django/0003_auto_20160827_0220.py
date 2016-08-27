# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_contact', '0002_auto_20160810_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='submit',
            new_name='submit_text',
        ),
        migrations.AlterField(
            model_name='contact',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_contact_contact', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='form_layout',
            field=models.CharField(help_text='Choice the layout of contact form', max_length=255, verbose_name='Form Layout', choices=[(b'cmsplugin_contact.forms.ContactForm', 'default')]),
        ),
    ]
