from to.models import Task
from django.shortcuts import render

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('update_at') # It will fetch task that are not completed
    context = {
        'tasks' : tasks,
    }
    
    return render(request, 'home.html')