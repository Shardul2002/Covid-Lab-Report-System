from dataclasses import field, fields
from django import forms

from CovidReportApp.models import Patients,ReportField;



class PatientForm(forms.ModelForm):
    class Meta:
        model=Patients
        fields='__all__'



class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model=ReportField
        fields='__all__'


class UpdatePatient(forms.ModelForm):
    class Meta:
        model=Patients
        fields='__all__'