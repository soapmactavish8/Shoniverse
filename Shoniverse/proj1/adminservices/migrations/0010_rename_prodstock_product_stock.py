# Generated by Django 4.0.6 on 2022-07-29 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminservices', '0009_product_prod_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prodStock',
            new_name='stock',
        ),
    ]
