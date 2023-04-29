from django.shortcuts import render
from django.contrib.auth import login
# register/signin form
from django.contrib.auth.forms import UserCreationForm


from .models import Workout







def index(request):
    return render(request, 'main_app/index.html')


# def about(request):
#   return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def workouts_index(request):
  workoutss = Workout.objects.all()
  return render(request, 'workouts/index.html', { 'workouts': workouts })