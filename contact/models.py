from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    # CharField é um campo de preenchimento obrigatório
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20) 
    phone = models.CharField(max_length=9)
    email = models.EmailField(max_length=100, blank=True) # Permitedeixar o campo vazio
    created_date = models.DateTimeField(default=timezone.now)
    # Nota: Tem de importar from django.utils import timezone
    # Não esquecer de ir a settings.py e alterar o LANGUAGE_CODE para 'pt-pt'
    # e o TIMEZONE para 'Europe/Lisbon'
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True,upload_to='pictures/%Y/%m/')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'