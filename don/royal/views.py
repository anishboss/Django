from django.shortcuts import render,redirect
from .models import Employee
from django.http import HttpResponse
from . forms import EmployeeForm


def index(request,id=0):
	if request.method == 'GET':
		if id==0:
			employee = EmployeeForm()
		else:
			data = Employee.objects.get(pk=id)
			employee = EmployeeForm(instance=data)
		return render(request,'index.html',{'employee':employee})
	else:
		if id==0:
			employee = EmployeeForm(request.POST)
		else:
			 data = Employee.objects.get(pk=id)
			 employee = EmployeeForm(request.POST,instance=data)
		if employee.is_valid():
			employee.save()
		return redirect('/list')

def list(request):
	employee = Employee.objects.all()
	return render(request,'list.html',{'employees':employee})

def employee_delete(request,id=0):
	employee = Employee.objects.get(pk=id)
	employee.delete()
	return redirect('list')
