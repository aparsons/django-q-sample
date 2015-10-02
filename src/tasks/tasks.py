from django_q.tasks import async




def email_hook(task):
    if task.success:
        print('Success')
    else:
        print('Nope')
