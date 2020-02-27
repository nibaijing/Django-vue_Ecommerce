# Generated by Django 3.0.3 on 2020-02-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('productdescription', models.CharField(max_length=200)),
                ('productcategory', models.CharField(max_length=200)),
                ('productprice', models.CharField(max_length=200)),
                ('productImage', models.CharField(max_length=200)),
                ('productseller', models.CharField(max_length=200)),
                ('isBestproduct', models.BooleanField()),
                ('isTopproduct', models.BooleanField()),
                ('productrating', models.IntegerField()),
            ],
        ),
    ]
