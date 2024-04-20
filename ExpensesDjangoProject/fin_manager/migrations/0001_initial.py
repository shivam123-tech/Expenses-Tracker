
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField(default=0)),
                ('end_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Liability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField(default=0)),
                ('date', models.DateField(null=True)),
                ('long_term', models.BooleanField(default=False)),
                ('interest_rate', models.FloatField(default=0)),
                ('end_date', models.DateField()),
                ('monthly_expense', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField(default=0)),
                ('return_rate', models.FloatField(default=0)),
                ('end_date', models.DateField()),
                ('return_amount', models.FloatField(default=0)),
                ('monthly_return', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.FloatField(default=0)),
                ('income', models.FloatField(default=0)),
                ('expense', models.FloatField(default=0)),
                ('saving_goal', models.FloatField(default=0)),
                ('salary', models.FloatField(default=0)),
                ('investment_list', models.ManyToManyField(blank=True, to='fin_manager.investments')),
                ('liability_list', models.ManyToManyField(blank=True, to='fin_manager.liability')),
                ('subscription_list', models.ManyToManyField(blank=True, to='fin_manager.subscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]