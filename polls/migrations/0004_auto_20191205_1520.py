# Generated by Django 2.2.6 on 2019-12-05 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20191204_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='club',
            field=models.CharField(choices=[('Alcheringa', 'Alcheringa'), ('Cadence', 'Cadence'), ('Anchorenza and RadioG (AnR)', 'Anchorenza and RadioG (AnR)'), ('Fine Arts', 'Fine Arts'), ('Montage', 'Montage'), ('Lumiere', 'Lumiere'), ('Octaves', 'Octaves'), ('Expressions', 'Expressions'), ('LitSoc-DebSoc', 'LitSoc-DebSoc'), ('Aeromodelling', 'Aeromodelling'), ('Astronomy', 'Astronomy'), ('Coding', 'Coding'), ('Consulting and Analytics (CnA)', 'Consulting and Analytics (CnA)'), ('Electronics ', 'Electronics '), ('Prakriti ', 'Prakriti '), ('Finance and Economics', 'Finance and Economics'), ('Robotics', 'Robotics '), ('ACUMEN', 'ACUMEN'), ('TechEvince', 'TechEvince'), ('Green Automobile', 'Green Automobile'), ('Entrepreneurial Development Cell (EDC)', 'Entrepreneurial Development Cell (EDC)'), ('Udgam', 'Udgam'), ('Techniche', 'Techniche'), ('None', 'None')], default='None', max_length=120),
        ),
        migrations.AddField(
            model_name='question',
            name='department',
            field=models.CharField(choices=[('Chemical Engineering', 'Chemical Engineering'), ('Biotechnology', 'Biotechnology'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Engineering Physics', 'Engineering Physics'), ('Mathematics and Computing', 'Mathematics and Computing'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Design ', 'Design '), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('None', 'None')], default='None', max_length=120),
        ),
    ]
