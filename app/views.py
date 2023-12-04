from django.shortcuts import render

# Create your views here.
def alert(request):
    return render(request,'alert.html')
def badges(request):
    return render(request,'badges.html')
def buttongroup(request):
    return render(request,'buttongroup.html')
def collapse(request):
    return render(request,'collapse.html')
def dropdown(request):
    return render(request,'dropdown.html')
def form(request):
    return render(request,'form.html')
def jumbotron(request):
    return render(request,'jumbotron.html')
def listgroup(request):
    return render(request,'listgroup.html')
def modals(request):
    return render(request,'modals.html')
def nav(request):
    return render(request,'nav.html')