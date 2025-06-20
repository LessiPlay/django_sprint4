from django import forms
from django.utils import timezone
from blog.models import Comment, Post, User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'rows': '4'}),
        }


class PostForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        initial=timezone.now(),
        label='Дата и время публикации',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )

    class Meta:
        model = Post
        exclude = (
            'author',
            'is_published',
        )
        widgets = {
            'text': forms.Textarea(attrs={'rows': '5'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
