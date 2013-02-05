from django.contrib import admin
from books.models import Editorial, Autor, Libro

admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Libro)