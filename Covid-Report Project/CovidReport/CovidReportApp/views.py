from audioop import reverse
from statistics import mode
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UpdatePatient
from CovidReportApp.forms import ClinicalDataForm,UpdatePatient
from CovidReportApp.models import ReportField
from CovidReportApp.models import Patients
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy 
# Create your views here.

@login_required
def home(request):
    return render(request,'CovidReportApp/index.html')


class PatientView(LoginRequiredMixin, ListView):
    model=Patients


class PatientCreateView(LoginRequiredMixin,CreateView):
    model= Patients
    success_url=reverse_lazy('display')
    fields=('FirstName','LastName','Age','Gender')
    


def PatientUpdateView(request,**kwargs):
    form=UpdatePatient
    patient=Patients.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=UpdatePatient(request.POST,instance=patient)
        if form.is_valid():
            form.save()
        return redirect('display')
    return render(request,'CovidReportApp/update_form.html',{'form':form,'patient':patient})
    


class PatientDeleteView(DeleteView):
    model= Patients
    success_url=reverse_lazy('display')


def addData(request,**kwargs):
    form=ClinicalDataForm()
    patient=Patients.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'CovidReportApp/coviddata_form.html',{'form':form,'patient':patient})


def analyze(request,**kwargs):
    patient=ReportField.objects.get(patient_id=kwargs['pk'])
    info=Patients.objects.get(id=kwargs['pk'])
    return render(request,'CovidReportApp/report.html',{'patient':patient,'info':info})


def logout(request):
    return render(request,'CovidReportApp/logout.html')