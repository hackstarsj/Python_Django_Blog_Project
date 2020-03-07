from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import BlogPosts
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


# Create your views here.
def hello(dara):
    print(dara)
    return HttpResponse("<h1>Hello World</h1>")

def showAllData(req):
    latest_question_list = BlogPosts.objects.all()
    for data in latest_question_list:
        print(data.title)


    return render(req,"data.html",{'data': latest_question_list})

def showSinglPost(req,link_url):
    data=BlogPosts.objects.get(url_slug=link_url)
    print(data.title)
    return render(req,"datasing.html",{'data':data})

@login_required(login_url="/login/")
def AddData(req):
    return render(req,"form.html")

def SaveData(req):
    if req.method=="POST":
        print("Post")
    else:
        print(req.method)
    print(req.POST.get("title",""))

    myfile = req.FILES['image']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = filename
    print(filename)
    #print(req.FILES['image'])

    blog=BlogPosts(title=req.POST.get("title",""),description=req.POST.get("description",""),url_slug=req.POST.get("url_slug",""),contents=req.POST.get("contents",""),published=req.POST.get("published",""),created_at=req.POST.get("created_at",""),image=uploaded_file_url)
    blog.save()
    print("ID : "+str(blog.pk))

    return HttpResponse("Data")

def UpdateData(req):
    blog=BlogPosts.objects.get(id=req.POST.get("id",""))
    if blog!=None:
        blog.title=req.POST.get("title","")
        blog.save()

    return HttpResponse("Updated")

def DeleteData(req,post_id):
    blog=BlogPosts.objects.get(id=post_id)
    blog.delete()
    return HttpResponseRedirect('/datashow')

def RegisterUsers(req):
    return render(req,"reg_user.html")

def Save_user(req):
    username = req.POST.get('username','')
    email = req.POST.get('email','')
    password = req.POST.get('password')
    if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
        User.objects.create_user(username, email, password)
        return HttpResponseRedirect('/register_user/Registered Successfully')
    else:
        return HttpResponseRedirect('/register_user/Email Already Exist')

        # url = reverse('register_user', kwargs={'error_data': 'Email Already Exist'})
        # return HttpResponseRedirect(url)


def RegisterUsersData(req,error_data):
    return render(req,"reg_user.html",{'error_data':error_data})

def Login(req):
    return render(req,'login_form.html')

def LoginRequest(req):
    user = authenticate(username=req.POST.get('username',''),password=req.POST.get('password',''))

    if user!=None:
        login(req, user)
        return HttpResponse("Logged IN")
    else:
        return HttpResponse("Invalid Login")

def User_home(req):
    return render(req,"home.html")


def LogOut(req):
    logout(req)
    return HttpResponseRedirect("login")


def index(request):
    return render(request, 'chat.html', {})

def room(request, room_name,person_name):
    return render(request, 'room.html', {
        'room_name': room_name,
        'person_name':person_name
    })

def template_example_1(request):
    return render(request,"child_page_1.html")

def template_example_2(request):
    return render(request,"child_page_2.html")