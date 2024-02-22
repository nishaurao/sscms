#from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm



#create a function

def user_list(request):
    data= User.objects.all()
    mydict={'data': data}
    return render(request, "ListingPage.html", context=mydict)


    

def AddUser(request):
    mydict = {}
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/sscsmsite/')
    mydict['form'] = form
    return render(request,'Add.html',mydict)


def EditUser(request, id=None):
    content = User.objects.get(id = id)
    form = UserForm(request.POST or None, request.FILES or None, instance = content)
    if form.is_valid():
        form.save()
        return redirect('/sscsmsite/')

    mydict = {'form': form}
    return render(request,'Edit.html',context=mydict)


def DeleteUser(request, id=None):
    content = User.objects.get(id = id)
    if request.method=="POST":
       content.delete()
       return redirect('/sscsmsite/')
    return render(request,'Delete.html')

def ViewUser(request,id=None):
    context={}
    content = User.objects.get(id=id)
    context['user']=content
    return render(request,'View.html',context)
