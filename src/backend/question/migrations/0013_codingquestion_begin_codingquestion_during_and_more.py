# Generated by Django 4.1.4 on 2023-10-26 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0012_remove_problemfrequency_qtype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='codingquestion',
            name='begin',
            field=models.CharField(default='text', max_length=4000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='codingquestion',
            name='during',
            field=models.CharField(default='text', max_length=4000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='codingquestion',
            name='finish',
            field=models.CharField(default='text', max_length=4000),
            preserve_default=False,
        ),
    ]