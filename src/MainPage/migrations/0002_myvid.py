# Generated by Django 3.1.3 on 2021-01-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyVid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vid', models.FileField(upload_to='videos/')),
            ],
        ),
    ]