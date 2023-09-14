from django.http import HttpResponseRedirect
from django.shortcuts import render
from service.models import Service
def login(request):
    return render(request,"signin.html")

def Home(request):
    servicesData = Service.objects.all().order_by('-pk')
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            funData = request.POST.get("funData")
            service = Service(name=name,funData=funData)
            service.save()
            return HttpResponseRedirect("/")
    except:
        pass
    return render(request,"index.html", {"servicesData":servicesData})


def Share(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            funData = request.POST.get("funData")
            service = Service(name=name,funData=funData)
            service.save()
            return HttpResponseRedirect("/")
    except:
        pass
    return render(request,"share.html")
