from django import forms
from .models import Project, Skill

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link', 'skills']
        widgets = {
            'skills': forms.CheckboxSelectMultiple()  # lets you select multiple skills
        }

# --- NEW: Form to add a Skill ---
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']