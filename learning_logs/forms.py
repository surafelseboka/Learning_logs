from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # fixed typo from 'lables'

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}  # fixed typo from 'lables'
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

