# Generated by Django 2.2.12 on 2020-05-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20200512_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageUpload', models.ImageField(upload_to='project-vue/src/assets/passport', verbose_name='Удостоверение')),
            ],
        ),
    ]
