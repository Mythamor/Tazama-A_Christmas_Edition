# Generated by Django 4.2.5 on 2023-11-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=1000)),
                ("image", models.ImageField(upload_to="movies")),
                (
                    "genres",
                    models.CharField(
                        choices=[
                            ("action", "ACTION"),
                            ("adventure", "ADVENTURE"),
                            ("animation", "ANIMATION"),
                            ("comedy", "COMEDY"),
                            ("documentary", "DOCUMENTARY"),
                            ("drama", "DRAMA"),
                            ("family", "FAMILY"),
                            ("fantasy", "FANTASY"),
                            ("history", "HISTORY"),
                            ("horror", "HORROR"),
                            ("music", "MUSIC"),
                            ("mystery", "MYSTERY"),
                            ("sci-fi", "SCI-FI"),
                            ("tv-movie", "TV-MOVIE"),
                            ("thriller", "THRILLER"),
                            ("war", "WAR"),
                            ("western", "WESTERN"),
                        ],
                        max_length=20,
                    ),
                ),
                ("directors", models.CharField(max_length=100)),
                ("cast", models.CharField(max_length=1000)),
                ("year_of_production", models.DateField()),
                ("views_count", models.IntegerField(default=0)),
            ],
        ),
    ]