# Generated by Django 2.2.2 on 2020-05-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200528_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='auto_point2',
            field=models.IntegerField(default=-1, verbose_name='思考・判断・表現'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='auto_point',
            field=models.IntegerField(default=-1, verbose_name='知識・技能'),
        ),
    ]
