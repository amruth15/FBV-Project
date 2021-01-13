from django.contrib import admin
from myApp.models import Emp

class EmpAdm(admin.ModelAdmin):
    l = ['eno','ename','esal','eaddr']
    
admin.site.register(Emp,EmpAdm)
