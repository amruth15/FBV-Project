import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','FBVProject1.settings')
django.setup()
from faker import Faker
from myApp.models import Emp

f = Faker()
def pop(n):
    for i in range(n):
        fno = f.random_int(min=1,max=20)
        fname = f.name()
        fsal = f.random_int(min=100000,max=500000)
        faddr = f.address()
        e = Emp.objects.get_or_create(eno=fno,ename=fname,esal=fsal,eaddr=faddr)
pop(20)
