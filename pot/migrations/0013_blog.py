# Generated by Django 4.2.5 on 2024-06-14 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pot', '0012_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='blog_thumbnails/')),
                ('published_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='pot.category')),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
