# Generated by Django 3.1.2 on 2020-11-04 09:51

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbourhood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('hood_photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField()),
                ('health_number', models.IntegerField(blank=True, null=True)),
                ('police_number', models.IntegerField(blank=True, null=True)),
                ('occupant_count', models.IntegerField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='avatar',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact',
        ),
        migrations.AddField(
            model_name='profile',
            name='national_id',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('1', 'Crimes and Safety'), ('2', 'Health Emergency'), ('3', 'Recommendations'), ('4', 'Fire Breakouts'), ('5', 'Lost and Found'), ('6', 'Death'), ('7', 'Event')], max_length=120)),
                ('title', models.CharField(max_length=100, null=True)),
                ('article', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_post', to='neighbourhood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='neighbourhood.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='neighbourhood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='neighbourhood.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='neighbourhood.neighbourhood'),
        ),
    ]
