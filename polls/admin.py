from django.contrib import admin
from .models import Question, Choice


class ChoiceRow(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question: ", {"fields":["question_text"]}),
        ("Date: ", {"fields":["pub_date"]}),

    ]
    inlines = [ChoiceRow]

admin.site.register(Question, QuestionAdmin)


