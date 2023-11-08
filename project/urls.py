
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage, name="homePage"),
    path('signupPage/',views.signupPage, name="signupPage"),
    path('loginPage/',views.loginPage, name="loginPage"),
    path('detailPage/',views.detailPage, name="detailPage"),
    path('dataPage/',views.dataPage, name="dataPage"),
    path('addPage', views.addPage,name="addPage"),
    path('editPage', views.editPage,name="editPage"),
    path('updatePage/<str:id>', views.updatePage,name="updatePage"),
    path('deletePage/<str:id>', views.deletePage,name="deletePage"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
