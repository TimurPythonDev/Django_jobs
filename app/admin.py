from django.contrib import admin

from app.models import City
from .models import City, Language, Vacancy


admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacancy)
