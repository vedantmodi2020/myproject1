from django import forms
from django.forms import fields
from .models import Post, Topic
from boards import models

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )
    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm) :
    class Meta:
        model = Post
        fields = ['message', ]