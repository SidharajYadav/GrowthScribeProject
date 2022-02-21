from django.shortcuts import render

from . import models


'''def contact(request):
    thank=False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
    return render(request, 'shop/contact.html', {'thank':thank}) '''

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        ins = models.contact(name=name, email=email, desc=desc)
        ins.save()
        print("Save in Database")
    return render(request,  'contact.html')

