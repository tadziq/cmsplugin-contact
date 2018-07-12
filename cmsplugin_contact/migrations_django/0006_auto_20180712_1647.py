# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_contact', '0005_auto_20180701_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='form_layout',
            field=models.CharField(verbose_name='Form Layout', max_length=255, choices=[('cmsplugin_contact.forms.ContactForm', 'default')], help_text='Choose the layout of contact form'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='recaptcha_size',
            field=models.CharField(verbose_name='ReCAPTCHA size', max_length=20, default='normal', choices=[('normal', 'Normal'), ('compact', 'Compact')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='recaptcha_theme',
            field=models.CharField(verbose_name='ReCAPTCHA theme', max_length=20, default='light', choices=[('light', 'Light'), ('dark', 'Dark')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='spam_protection_method',
            field=models.SmallIntegerField(verbose_name='Spam protection method', default=0, choices=[(0, 'Honeypot'), (1, 'Akismet'), (2, 'ReCAPTCHA')]),
        ),
    ]
