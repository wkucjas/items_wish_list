from django.db import models

# Create your models here.


class Item(models.Model):
    item_text = models.CharField(max_length=200)
    item_link = models.URLField()

    def __str__(self):
        return self.item_text

    def get_item_link(self):
        return self.item_link
