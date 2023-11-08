from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login 
from myapp.models import Members

def homePage(request):
    
    return render(request,'index.html')

def signupPage(request):
     if request.method=="POST":
          name=request.POST.get("name")
          email=request.POST.get("email")
          password=request.POST.get("pass")
          re_password=request.POST.get("re_pass")

          if password == re_password:
            return HttpResponse('<h1 style="background-color:violet;color:white;padding:20px;text-align:center;">Your password did not match! 😕<h1><br><img src="../static/images/pass_not_match.jpg" alt="">')
          else:
              myuser=User.objects.create_user(name,email,password)
              myuser.save()
              return redirect("dataPage")
    
     return render(request,'signup.html')

def loginPage(request):
    if request.method=="POST":
        email=request.POST.get("email")
        pass1=request.POST.get("password")
        user=authenticate(request,username=email,password=pass1)
        
        if user is None:
            login(request,user)
            return redirect("dataPage")
        else:
            return HttpResponse("username not found")
    
    return render(request,"login.html")

def detailPage(request):
     user=request.user
     emp=Members.objects.all()
     context={
         'emp':emp   
    }
    
    # return render(request,"home.html",)

     return render(request, 'detail.html', {'user_name': user, 'emp': emp})


def dataPage(request):
    
    return render(request,'data.html')

def addPage(request):
      if request.method=="POST":
        myName=request.POST.get("name")
        myEmail=request.POST.get("email")
        myAddress=request.POST.get("address")
        myPhone=request.POST.get("phone")
        
        emp=Members(
            name=myName,
            email=myEmail,
            address=myAddress,
            phone=myPhone
            
        )
        
        emp.save()
        return redirect("detailPage")
        
        
      return render(request,"detail.html")

def editPage(request):
    
    emp=Members.objects.all()
    
    content={
        "emp":emp
    }
    
    return render(request,"home.html",content)


def updatePage(request,id):

    if request.method=="POST":
        myName=request.POST.get("name")
        myEmail=request.POST.get("email")
        myAddress=request.POST.get("address")
        myPhone=request.POST.get("phone")
        
        emp=Members(
            id=id,
            name=myName,
            email=myEmail,
            address=myAddress,
            phone=myPhone
            
        )
        
        emp.save()
        return redirect("detailPage")
        
        
    return render(request,"detail.html")


def deletePage(request,id):
    
    emp=Members.objects.filter(id=id)
    emp.delete()
    return redirect("detailPage")