from django.contrib import admin
from .models import Question, Answer, Category

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category.name']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Category, CategoryAdmin)

