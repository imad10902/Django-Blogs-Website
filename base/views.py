from django.shortcuts import render, redirect
from .forms import UserForm, BlogForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser, Blog


def home(request):
    return render(request, "base/home.html")


def blogsPage(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    if q == "":
        blogs = Blog.objects.all()
    else:
        blogs = Blog.objects.filter(category=q)

    context = {"blogs": blogs}
    return render(request, "base/blogs.html", context)


def createBlog(request):
    form = BlogForm()

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect("blogs")
        else:
            messages.error(request, "An error occured")

    context = {"form": form}
    return render(request, "base/create_blog.html", context)


def blogDetail(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {"blog": blog}
    return render(request, "base/blog_view.html", context)


def editBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("blogs")
        else:
            messages.error(request, "Could Not edit")

    context = {"form": form}
    return render(request, "base/create_blog.html", context)


def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return redirect("blogs")

    return render(request, "base/delete_blog.html")


def myBlogsPage(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    if q == '':
        blogs = Blog.objects.filter(author=request.user)
        page = 'myblogs'
    else:
        blogs = Blog.objects.filter(draft='YES', author=request.user)
        page = 'drafts'

    context = {"blogs": blogs, 'page': page}
    return render(request, "base/myblogs.html", context)


def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = CustomUser.objects.get(
                username=username
            )  # check if username in the database
        except:
            messages.error(request, "User does not exist")

        user = authenticate(
            request, username=username, password=password
        )  # authentication step

        if user is not None:
            login(request, user)  # this user object is being used in templates
            return redirect("home")
        else:
            messages.error(request, "Username or password does not exist")

    context = {"page": page}
    return render(request, "base/login_register.html", context)


def registerPage(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(
                commit=False
            )  # create user class instance but not push to database
            user.username = (
                user.username.lower()
            )  # convert into lowercase to ease searching while logging in
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occured")

    context = {"form": form}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")
