from to.models import Task
from django.shortcuts import render

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('update_at') # It will fetch task that are not completed
    completed_tasks = Task.objects.filter(is_completed = True) # It will have task that are tham completed
    context = {
        'tasks' : tasks,
        'completed_tasks' : completed_tasks
    }
    return render(request, 'home.html')