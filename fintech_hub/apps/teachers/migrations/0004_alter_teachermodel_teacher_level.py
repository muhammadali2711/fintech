# Generated by Django 4.1 on 2022-12-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_teachermodel_teacher_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='teacher_level',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], max_length=255),
        ),
    ]