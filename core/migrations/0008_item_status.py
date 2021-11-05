# Generated by Django 2.2.14 on 2021-10-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_item_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('S', 'Sale'), ('H', 'HOT')], max_length=1, null=True),
        ),
    ]
