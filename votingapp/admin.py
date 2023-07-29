from django.contrib import admin
# Register your models here.
from .models import Question, Choice
 
admin.site.site_header = "Voting Admin"
admin.site.site_title = "Voting Admin Area"
admin.site.index_title = "Welcome to the Voting Admin Area"
 
 
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3 # to add the option column in admin panel default number will as in extra field
 
 
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question', {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date']}), ]
    inlines = [ChoiceInLine]
    #This means that when you edit a question, you will be able to add, edit and delete that question's choices at the same time.
    #otherwise we can only edit the question and date information 
    #fieldsets is a list of two-tuples, in which each two-tuple represents a <fieldset> on the admin form page. (A <fieldset> is a “section” of the form.)
    #The two-tuples are in the format (name, field_options), where name is a string representing the title of the fieldset and field_options is a dictionary of information about the fieldset, including a list of fields to be displayed in it.
    #'classes': ['collapse'] can be added if we want to hide show date information
    
 
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
#This is invalid, because we can't register a model with an Inline. You can only register a model with a ModelAdmin class.