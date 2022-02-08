from django.contrib import admin

from .models import Question

# TODO add custom QuestionAdmin for inline add, edit and create Choices of Question

admin.site.register(Question)
