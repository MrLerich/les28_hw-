from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, verbose_name='Автор', related_name='ads', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=400)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name
