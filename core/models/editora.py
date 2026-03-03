from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=2500)
    site = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome