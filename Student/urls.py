from django.urls import path

from Student import views

urlpatterns = [
    #studentapp urls
    path('',views.home,name='home'),
    path('display',views.display,name='displaystudents'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('edit/<int:id>',views.editstudent,name='editstudent'),
    path('delete/<int:id>', views.deletestudent, name='deletestudent'),
    #login system urls
    path('login',views.login_fun,name='login'),
    path('register',views.register_fun,name='register'),
    path('logout',views.logout_fun,name='logout')



]