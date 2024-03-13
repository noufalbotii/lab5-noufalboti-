from django.shortcuts import render, redirect



class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

people = []

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = Person(username=username, password=password)
        people.append(new_person)
        return redirect('/')
    return render(request, 'myapp/add.html')

def show_people(request):
    return render(request, 'myapp/show.html', {'people': people})