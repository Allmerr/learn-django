# Generated by Django 4.1.3 on 2022-12-08 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_keterangan_buku_keterangan_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buku',
            old_name='keterangan_id',
            new_name='keterangan',
        ),
    ]