import email
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User 

# Create your views here.
def add_show(request):
 if request.method == 'POST':
    fm=StudentRegistration(request.POST)
    if fm.is_valid():
        nm=fm.cleaned_data['vehiclename']
        em=fm.cleaned_data['vehicleowner']
        pw=fm.cleaned_data['password']
        reg=User(vehilename=nm, vehicleowner=em, password=pw)
        reg.save()
        fm=StudentRegistration()
 else:
    fm=StudentRegistration()
 stud=User.objects.all()
 return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})

def delete_data(request):
    if request.method=='post':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
