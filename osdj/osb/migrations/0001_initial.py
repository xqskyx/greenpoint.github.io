# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=1024, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('createdate', models.DateTimeField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\xb0\x8f\xe7\xbb\x84\xe5\x90\x8d\xe7\xa7\xb0')),
                ('createdate', models.DateTimeField(null=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('description', models.CharField(max_length=360, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('image', models.ImageField(upload_to=b'groupImages', null=True, verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=128, verbose_name=b'\xe8\xaf\x9d\xe9\xa2\x98\xe6\xa0\x87\xe9\xa2\x98')),
                ('description', models.CharField(max_length=512, verbose_name=b'\xe8\xaf\x9d\xe9\xa2\x98\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('createdate', models.DateTimeField(null=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('group', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\xb0\x8f\xe7\xbb\x84', to='osb.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=16, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('truename', models.CharField(max_length=32, null=True, verbose_name=b'\xe7\x9c\x9f\xe5\x90\x8d', blank=True)),
                ('nowcity', models.CharField(max_length=42, null=True, verbose_name=b'\xe7\x8e\xb0\xe5\xb1\x85\xe5\x9f\x8e\xe5\xb8\x82', blank=True)),
                ('soldiercity', models.CharField(max_length=42, verbose_name=b'\xe6\x9c\x8d\xe5\xbd\xb9\xe5\x9c\xb0\xe7\x82\xb9')),
                ('joindate', models.DateField(verbose_name=b'\xe5\x85\xa5\xe4\xbc\x8d\xe5\xb9\xb4\xe4\xbb\xbd')),
                ('email', models.EmailField(max_length=75, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('sex', models.CharField(max_length=4, null=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', blank=True)),
                ('state', models.BooleanField(default=False, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81')),
                ('birthday', models.DateField(null=True, verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5', blank=True)),
                ('telphone', models.CharField(max_length=14, null=True, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d', blank=True)),
                ('picture', models.ImageField(upload_to=b'userImages', null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='topics',
            name='likeduser',
            field=models.ManyToManyField(related_name='likegroupuser', null=True, verbose_name=b'\xe5\x96\x9c\xe6\xac\xa2\xe7\x9a\x84\xe4\xba\xba', to='osb.User', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(verbose_name=b'\xe7\xbb\x84\xe9\x95\xbf', to='osb.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(related_name='groupmemberuser', null=True, to='osb.User', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='commenter',
            field=models.ManyToManyField(related_name='commentcommentuser', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85', to='osb.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='likeduser',
            field=models.ManyToManyField(related_name='likecommentsuser', verbose_name=b'\xe5\x96\x9c\xe6\xac\xa2\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7', to='osb.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(blank=True, to='osb.Comments', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='topics',
            field=models.ForeignKey(to='osb.Topics'),
            preserve_default=True,
        ),
    ]
