# Generated by Django 4.2.2 on 2023-06-25 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('category', models.CharField(choices=[('HEART DISEASE', 'HEART DISEASE'), ('EAR PROBLEMS', 'EAR PROBLEMS'), ('COVID-19', 'COVID-19'), ('EYE PROBLEMS', 'EYE PROBLEMS')], default='HEART DISEASE', max_length=20)),
                ('summary', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
