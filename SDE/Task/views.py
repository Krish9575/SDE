from django.shortcuts import render

# Create your views here.
def task_view(request):
    First_name="krishna"
    Last_name="Maru"
    return render(request,'Task/task.html',{'fm':First_name,'lm':Last_name})
