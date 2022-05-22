# Generated by Django 4.0.4 on 2022-05-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(max_length=100)),
                ('School', models.CharField(max_length=200)),
                ('School_marks', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('Degree', models.CharField(max_length=200)),
                ('University', models.CharField(max_length=200)),
                ('Degree_percentage', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('skill', models.CharField(max_length=100)),
                ('previous_roll', models.CharField(max_length=100)),
                ('previous_experience', models.CharField(max_length=20)),
                ('Tech_skill', models.CharField(max_length=100)),
                ('job_city', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, upload_to='profileimg')),
                ('file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]