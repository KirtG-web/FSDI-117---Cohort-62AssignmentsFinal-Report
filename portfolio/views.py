from django.shortcuts import render, redirect
from .models import Project, Skill
from .forms import ProjectForm, SkillForm  # make sure SkillForm is imported

# --- existing views ---
def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def experience(request):
    return render(request, 'portfolio/experience.html')

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': all_projects})

def skills(request):
    all_skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': all_skills})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/add_project.html', {'form': form})

# --- NEW view to add skill ---
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills')  # go back to skills page after saving
    else:
        form = SkillForm()
    return render(request, 'portfolio/add_skill.html', {'form': form})