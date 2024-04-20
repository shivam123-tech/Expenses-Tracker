
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_manager', '0002_alter_liability_date_alter_liability_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='user',
        ),
        migrations.RemoveField(
            model_name='account',
            name='investment_list',
        ),
        migrations.RemoveField(
            model_name='account',
            name='subscription_list',
        ),
        migrations.AlterField(
            model_name='liability',
            name='date',
            field=models.DateField(default=datetime.date(2023, 8, 18)),
        ),
        migrations.DeleteModel(
            name='Investments',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
