"""finsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view,Code_view,About_view,Accmassage_view,AccNumber_view,AccrRecl_view,AccRec_view,AccRecOrg_view,AddEditUser_view,AppSettings_view,ApprDateSet_view,ApprReqTrn_view,AutoBatch_view,BackDateRol_view,Backup_view,BalOff_view,BatList_view,BatNew_view, BatTrn_view,BrDet_view,BrLang_view,Brow_view,CapEditSign_view,CenMetDate_view,ChgCID_view,ChgCIDApp_view,ChgIntMode_view,ChgIntRate_view,ChgSinTory_view,ChgUserPass_view,Chrg_view,ChrOfAcc_view,ChqPrVoid_view,ChqPrLoan_view,ChqPrLoanA_view,ChqPrLoanApr_view,ChqBook_view,ChqBookCan_view,ChqDep_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
