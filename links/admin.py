from django.contrib import admin
from .models import Link

admin.site.register(Link)
#admin.site.register(Link, LinkAdmin)
# Register your models here.
# @app.register(Link)
# class LinkAdmin(admin.ModelAdmin):
#     pass

