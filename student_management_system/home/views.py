from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from .models import User,Course,Student,Teacher
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        pwd=make_password(request.POST['pwd'])
        if User.objects.filter(name=name).exists():
            messages.info(request,'username is already exists ')
            return render(request,'temp/signup.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists ')
            return render(request,'temp/signup.html')    
        else:
            user=User.objects.create(name=name,email=email,password=pwd)
            user.save()
            messages.success(request,'!!!!! Sucessfully Registered !!!!!')
            return render(request,'temp/index.html')
    else:        
        return render(request,"temp/signup.html")

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd_user=request.POST['pwd']
        if User.objects.filter(email=email).exists():
            obj=User.objects.get(email=email)
            pwd=obj.password
            if check_password(pwd_user,pwd):
                return redirect('/dashboard')
            else:
                messages.error(request,' Password Incorrect')
                return render (request,'temp/index.html')                
        else:
            messages.error(request,' email is not registered')       
            return render(request,"temp/index.html") 
    else:       
        return render(request,"temp/index.html")

def index(request):
    return render (request,'temp/index.html')        

def lgout(request):
    auth.logout(request)
    messages.info(request,'sucessfully logout ')
    return render(request,'temp/index.html') 

def course(request):
    data=Course.objects.all()
    return render (request,'temp/course.html',{'data':data})
     

def addcourses(request):
    name=request.POST['name']
    fees=request.POST['fees']
    fees=int(fees)
    duration=request.POST['duration']
    textfield=request.POST['textfield']
    if Course.objects.filter(name=name).exists():
        messages.info(request,'Course already exists')
        data=Course.objects.all()
        return render(request,'temp/course.html',{'data':data}) 
    else:
        Course.objects.create(name=name, fees=fees,textfield=textfield,duration=duration)
        messages.success(request,'!!!!Successfully Added!!!!')
        data=Course.objects.all()
        return render(request,'temp/course.html',{'data':data}) 

def deletecourse(request):
    cid=request.GET['cid']
    Course.objects.get(id=cid).delete()
    data=Course.objects.all()
    return render(request,"temp/course.html",{'data':data}) 

def updatecourse(request):
    c=Course()
    c.id=request.POST['id'] 
    c.name=request.POST['name']
    fees=request.POST['fees']
    c.fees=int(fees)
    c.duration=request.POST['duration']
    c.textfield=request.POST['textfield']   
    c.save()
    data=Course.objects.all()
    return render(request,'temp/course.html',{'data':data})

def searchcourse(request):
    name=request.POST['name']
    e=Course.objects.get(name=name)
    return render(request,'temp/course.html',{'data':[e]})     

def addstudent(request):
    t=Student()
    t.name=request.POST['name']
    t.email=request.POST['email']
    t.contact=request.POST['contact']
    t.college=request.POST['college']
    t.degree=request.POST['degree']
    t.total=request.POST['total']
    t.paid=request.POST['paid']
    t.due=request.POST['due'] 
    tid=request.POST['course']
    t.course=Course.objects.get(id=tid)
    t.save()
    st=Student.objects.all()
    data=Course.objects.all()
    return render(request,'temp/viewstudents.html',{'st':st,'data':data})

def deletestudent(request):
    id=request.GET['id']
    Student.objects.filter(id=id).delete()
    data=Course.objects.all()
    st=Student.objects.all()
    return render(request,'temp/viewstudents.html',{'data':data,'st':st}) 

def updatestudent(request): 
    t=Student()
    t.id=request.POST['id']
    t.name=request.POST['name']
    t.email=request.POST['email']
    t.contact=request.POST['contact']
    t.college=request.POST['college']
    t.degree=request.POST['degree']
    tid=request.POST['course']
    t.course=Course.objects.get(id=tid)
    t.save()
    data=Course.objects.all()
    st=Student.objects.all()
    return render(request,'temp/viewstudents.html',{'data':data,'st':st})

def searchstudent(request):
    find=request.POST['name']
    s=Student.objects.filter(Q(name=find) | Q(email=find) | Q(college=find)).all()
    return render(request,'temp/viewstudents.html',{'st':s})                                   

def dashboard(request):
    data=Course.objects.all()
    count_course= Course.objects.all().count()
    count_student= Student.objects.all().count()
    count_teacher=Teacher.objects.all().count()
    return render (request,'temp/dashboard.html',{'data':data,'count_course':count_course,'count_student':count_student,'count_teacher':count_teacher})

def viewstudents(request):
    data=Course.objects.all()
    st=Student.objects.all()
    return render(request,'temp/viewstudents.html',{'data':data,'st':st})

def teacher(request):
    tech=Teacher.objects.all()
    return render(request,'temp/teacher.html',{'tech':tech})

def addteacher(request):
    name=request.POST['name']
    email=request.POST['email']
    join=request.POST['join']
    contact=request.POST['contact']
    education=request.POST['education']
    empid=request.POST['empid']
    empid=int(empid)
    exp=request.POST['exp']
    pack=request.POST['pack']
    if Teacher.objects.filter(email=email).exists():
        tech=Teacher.objects.all()
        return render(request,'temp/teacher.html',{'tech':tech}) 
    else:
        Teacher.objects.create(name=name,email=email,join=join,contact=contact,education=education,empid=empid,exp=exp,pack=pack)
        messages.success(request,'!!!!Successfully Added!!!!')
        tech=Teacher.objects.all()
        return render(request,'temp/teacher.html',{'tech':tech})

def deleteteacher(request):
    id=request.GET['id']
    Teacher.objects.filter(id=id).delete()
    tech=Teacher.objects.all()
    return render(request,'temp/teacher.html',{'tech':tech})
            
def updateteacher(request):
    c=Teacher()
    c.id=request.POST['id']     
    c.name=request.POST['name']
    c.email=request.POST['email']
    c.contact=request.POST['contact']
    c.join=request.POST['join']
    c.education=request.POST['education']
    c.empid=request.POST['empid']
    # c.empid=int(empid)
    c.exp=request.POST['exp']
    c.pack=request.POST['pack'] 
    c.save()
    tech=Teacher.objects.all()
    return render(request,'temp/teacher.html',{'tech':tech})

def searchteacher(request):
    find=request.POST['name']
    tech=Teacher.objects.filter(Q(name=find) | Q(email=find)).all()
    return render(request,'temp/teacher.html',{'tech':tech})    
