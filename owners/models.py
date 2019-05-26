from django.db import models

class Onw(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название фирмы')


def __str__(self):
    return self.name

#	дальше мы добавляем функцию для отображения на уровень выше
class Meta: 
    verbose_name='Владелец' 
#verbose_name_plural='Контрагенты'   
    ordering = ['name']
	
		

# Create your models here.
#