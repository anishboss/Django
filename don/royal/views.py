from django.shortcuts import render,redirect
from .models import Employee
from django.http import HttpResponse
from . forms import EmployeeForm


def index(request):
	if request.method == 'GET':
		employee = EmployeeForm()
		return render(request,'index.html',{'employee':employee})
	else:
		employee = EmployeeForm(request.POST)
		if employee.is_valid():
			employee.save()
		return redirect('/')

def list(request):
	employee = Employee.objects.all()
	return render(request,'list.html',{'employees':employee})

	