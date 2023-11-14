from django.shortcuts import render
from .models import Student
# Create your views here.
def myApp(request):
    if request.method == "POST":
        name = request.POST["name"]
        branch = request.POST["branch"]
        college = request.POST["college"]
        grade = request.POST["grade"]
        student = Student(name=name,branch=branch,college=college,grade=grade)
        student.save()

    # std = Student.objects.all()

    return render(request,"index.html")