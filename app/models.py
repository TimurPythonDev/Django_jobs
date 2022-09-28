from pyexpat import model
from django.db import models

from app.utils import from_crillic_to_eng



class City(models.Model):
    """City models """
    name = models.CharField(max_length=50,unique=True,verbose_name='Название населенного пункта')
    slug = models.CharField(max_length=50,unique=True,null=True,blank=True)

    class Meta:
        verbose_name = "Название населенного пункт"
        verbose_name_plural = "Название населенных пунктов"

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = from_crillic_to_eng(str(self.name))
        super().save(*args,**kwargs)


class Language(models.Model):
    
    name = models.CharField(max_length=50,unique=True,verbose_name='Язык программирования')
    slug = models.CharField(max_length=50,unique=True,null=True,blank=True)

    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Языки программирования"

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = from_crillic_to_eng(str(self.name))
        super().save(*args,**kwargs)

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250,verbose_name='Заголовок вакансии')
    company = models.CharField(max_length=250,verbose_name='Компания')
    description = models.TextField(verbose_name='Описания вакансии')
    city = models.ForeignKey('City',on_delete=models.CASCADE,verbose_name='Город')
    language = models.ForeignKey('Language',on_delete=models.CASCADE,verbose_name='Язык программирования')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансия"

    def __str__(self):
        return self.title
    
    