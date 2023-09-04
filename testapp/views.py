from django.shortcuts import render
from .models import Employeedata
from django.http.response import HttpResponse
from django. db. models import Q
import faker
import random

fake = faker.Faker()

def Empdata(request):
    for i in range(100):
        fname = fake.first_name()
        lname = fake.last_name()
        sal = fake.random_element(elements=(20000,10000,30000,40000))
        com = fake.random_element(elements=('TCS','WIPRO','INFOSYS','CTC'))
        city = fake.random_element(elements=('Hyd','Bang','Pune','Chennai'))
        email = fake.email()
        address = fake.address()

        Employeedata(
            first_name = fname,
            last_name = lname,
            salary = sal,
            company = com,
            city = city,
            email = email,
            address = address
        ).save()
    return HttpResponse('data saved')

def fetching(request):
    employees = Employeedata.objects.all()
    return render(request, 'index.html', {'employees':employees})

def homepage(request):
    return render(request, 'homepage.html')

def Hyderabad(request):
    if request.method =='GET':
        employees = Employeedata.objects.filter(city='Hyd')
        print(len(employees))
        return render(request,'hyderabad.html',{'employees':employees})
    else:
        company1 = request.POST.get('com')
        employees = Employeedata.objects.filter(Q(city='Hyd') & Q(company=company1))
        print(len(employees))
        return render(request,'hyderabad.html',{'employees':employees})



def Pune(request):
    if request.method =='GET':
        employees = Employeedata.objects.filter(city='Pune')
        print(len(employees))
        return render(request,'pune.html',{'employees':employees})
    else:
        company1 = request.POST.get('com')
        employees = Employeedata.objects.filter(Q(city='Pune') & Q(company=company1))
        print(len(employees))
        return render(request,'pune.html',{'employees':employees})


def Banglore(request):
    if request.method =='GET':
        employees = Employeedata.objects.filter(city='Bang')
        print(len(employees))
        return render(request,'banglore.html',{'employees':employees})
    else:
        company1 = request.POST.get('com')
        employees = Employeedata.objects.filter(Q(city='Bang') & Q(company=company1))
        print(len(employees))
        return render(request,'banglore.html',{'employees':employees})


def Chennai(request):
    if request.method =='GET':
        employees = Employeedata.objects.filter(city='Chennai')
        print(len(employees))
        return render(request,'chennai.html',{'employees':employees})
    else:
        company1 = request.POST.get('com')
        employees = Employeedata.objects.filter(Q(city='Chennai') & Q(company=company1))
        print(len(employees))
        return render(request,'chennai.html',{'employees':employees})


