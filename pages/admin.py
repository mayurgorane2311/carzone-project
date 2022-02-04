from django.contrib import admin
from . models import Team
from django.utils.html import format_html

# Register your models here.
class Teamadmin(admin.ModelAdmin):
    def photos(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))

# see if above ''photos'' function name different then we can change there name so follow
#assume that fuction name is ''thumnail'' and we want ''photos'' name so write below line
# thumnail.short_description = 'photos'

    list_display = ('id','photos','first_name','designation','created_date')
    list_display_links = ('id','first_name',)
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)

admin.site.register(Team,Teamadmin)
