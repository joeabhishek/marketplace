from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from django.contrib import admin
#from suit_ckeditor.widgets import CKEditorWidget
from suit_redactor.widgets import RedactorWidget
from marketplace.models import Extensions
from marketplace.models import Screenshots
from marketplace.models import ReleaseNotes
from suit.widgets import SuitDateWidget, SuitSplitDateTimeWidget, \
    EnclosedInput, LinkedSelect, AutosizedTextarea
from django.forms import TextInput


class ExtensionsForm(ModelForm):
    class Meta:
        model = Extensions
        widgets = {
            'name':  TextInput(attrs={'class': 'input-large'}),
            'description' : RedactorWidget(editor_options={'lang': 'en' , 'class' : 'input-mini'}),
            'authorName' : TextInput(attrs={'class': 'input-large'}),
            'license' : RedactorWidget(editor_options={'lang': 'en'})
        }


class ScreenshotsInline(admin.StackedInline):
    model = Screenshots
    extra = 0

class ReleaseNotesInlineForm(ModelForm):
    class Meta :
        widgets = {
            'version_number' : TextInput(attrs={'class': 'input-large'}),
            'change_log' : RedactorWidget(editor_options={'lang': 'en' }),
            'release_notes' : RedactorWidget(editor_options={'lang': 'en'})
        }

class ReleaseNotesInline(admin.StackedInline):
    model = ReleaseNotes
    form = ReleaseNotesInlineForm
    fieldsets = [
      (None ,{
          'fields': ('version_number','change_log','release_notes')
      }),
    ]
    extra = 0
    
    

class ExtensionsAdmin(admin.ModelAdmin):
    form = ExtensionsForm
    inlines = [ ScreenshotsInline,ReleaseNotesInline, ]
    fieldsets = [
      (None ,{
          'fields': ('name','description','authorName','license')
      }),
    ]



#class PersonAdmin(ModelAdmin):
 #   list_display = ('first_name','last_name','colored_name')
  #  list_filter = ('first_name')

    

admin.site.register(Extensions,ExtensionsAdmin)
