from django.shortcuts import render, redirect, get_object_or_404

from todoapp.models import Task


# Create your views here.
def home(request):
    task_completed = Task.objects.filter(is_completed=True)

    task_not_completed = Task.objects.filter(is_completed=False)
    context = {
        'task_completed': task_completed,
        'task_not_completed': task_not_completed,
    }
    return render(request, 'home.html', context)


def addtask(request):
    task = request.POST['task']
    image = request.FILES['image']

    Task.objects.create(task=task, image=image)
    return redirect('/')


def mark_done(request, pk):
    done = get_object_or_404(Task, pk=pk)
    done.is_completed = True
    done.save()
    return redirect('/')


def mark_undone(request, pk):
    undone = get_object_or_404(Task, pk=pk)
    undone.is_completed = False
    undone.save()
    return redirect('/')


def update(request, pk):
    update_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task = request.POST['task']
        image = request.FILES['image']
        update_task.task = task
        update_task.image = image
        update_task.save()
        return redirect('/')
    else:
        context = {
            'update_task': update_task,
        }
        return render(request, 'update.html', context)


def delete(request, pk):
    delete_task = get_object_or_404(Task, pk=pk)
    delete_task.delete()
    return redirect('/')
