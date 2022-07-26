# Generated by Django 4.0.6 on 2022-07-26 06:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('sold', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('info', models.TextField()),
                ('main_img', models.ImageField(upload_to='')),
                ('sub_img', models.ImageField(upload_to='')),
                ('category1', models.CharField(max_length=200)),
                ('catergory2', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='QnAs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='QnA_products', to='main.products')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Orders_products', to='main.products')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Orders_options', to='main.options')),
            ],
        ),
        migrations.AddField(
            model_name='options',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Options_products', to='main.products'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments_products', to='main.products')),
            ],
        ),
    ]
