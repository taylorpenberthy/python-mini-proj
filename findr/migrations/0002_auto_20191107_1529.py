# Generated by Django 2.2.7 on 2019-11-07 15:29

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('findr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.TextField()),
                ('cuisine', models.CharField(max_length=100)),
                ('restriction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='findr.Restriction')),
            ],
        ),
    ]
