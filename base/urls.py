from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sign-up", views.registerPage, name="sign-up"),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("blogs", views.blogsPage, name="blogs"),
    path("create-blog", views.createBlog, name="create-blog"),
    path("blog/<str:pk>", views.blogDetail, name="blog"),
    path("edit-blog/<str:pk>", views.editBlog, name="edit-blog"),
    path("delete-blog/<str:pk>", views.deleteBlog, name="delete-blog"),
    path("my-blogs", views.myBlogsPage, name="my-blogs"),
]
