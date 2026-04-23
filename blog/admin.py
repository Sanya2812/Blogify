from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Category,Post

#for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 3

    class Media:
        js=("https://cdn.tiny.cloud/1/c6bgdnq2sad4t1pjlvckaew8wr809yr9ic8ywmkdth5dfd4m/tinymce/7/tinymce.min.js" ,'js/script.js',)

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)