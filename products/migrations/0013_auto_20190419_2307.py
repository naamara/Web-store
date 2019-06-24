# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20190323_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeatured',
            name='image',
            field=models.ImageField(upload_to=b'ziramba_web/products/featured/'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'ziramba_web/products/'),
        ),
    ]
