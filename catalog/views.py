
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

def valid_id(id):
    valid = re.match("[0-9]+", id)
    if valid:
        return valid

# Create your views here.
def home(request):
    print(request.build_absolute_uri())
    return render(request, "catalog/index.html", { 'date': datetime.now() })

def edit(request, id):
    print(request.build_absolute_uri())
    now = datetime.now()
    if valid_id(id):
        msg = f"gathering product {id} info "
    else:
        msg = f"Incorrect value for parameter id"
    return render(request, "edit/edit.html", { 'msg':msg, 'id':id, 'date' : now })

def view(request, id):
    now = datetime.now()
    print(request.build_absolute_uri())
    if valid_id(id):
        msg = f"gathering product {id} info "
    else:
        msg = f"Incorrect value for parameter id"
    return render(request, "edit/edit.html", { 'msg':msg, 'id':id, 'date' : now })
