from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
	return render(request,"login.html",{})
def Code_view(*args, **kwargs):
	return HttpResponse("<h1>Code Page</h1>")
def About_view(*args, **kwargs):
	return HttpResponse("<h1>About Page</h1>")
def Accmassage_view(*args, **kwargs):
	return HttpResponse("<h1>Account Massage Page</h1>")
def AccNumber_view(*args, **kwargs):
	return HttpResponse("<h1>Account Number Page</h1>")
def AccrRecl_view(*args, **kwargs):
	return HttpResponse("<h1>Account Reclassification Page</h1>")
def AccRec_view(*args, **kwargs):
	return HttpResponse("<h1>Account Reclassification Page</h1>")
def AccRecOrg_view(*args, **kwargs):
	return HttpResponse("<h1>Account Reclassification Page</h1>")
def AddEditUser_view(*args, **kwargs):
	return HttpResponse("<h1>Add/Edit User Page</h1>")
def AppSettings_view(*args, **kwargs):
	return HttpResponse("<h1>Application Setting Page</h1>")
def ApprDateSet_view(*args, **kwargs):
	return HttpResponse("<h1>Approve Date Range Page</h1>")
def ApprReqTrn_view(*args, **kwargs):
	return HttpResponse("<h1>Approve Record Transaction Page</h1>")
def AutoBatch_view(*args, **kwargs):
	return HttpResponse("<h1>Auto Batch Page</h1>")
def BackDateRol_view(*args, **kwargs):
	return HttpResponse("<h1>Back Date Rollover Page</h1>")
def Backup_view(*args, **kwargs):
	return HttpResponse("<h1>Backup Page</h1>")
def BalOff_view(*args, **kwargs):
	return HttpResponse("<h1>Balance off Page</h1>")
def BatList_view(*args, **kwargs):
	return HttpResponse("<h1>Batch List Page</h1>")
def BatNew_view(*args, **kwargs):
	return HttpResponse("<h1>New Batch Page</h1>")
def BatTrn_view(*args, **kwargs):
	return HttpResponse("<h1>Batch Transaction Page</h1>")
def BrDet_view(*args, **kwargs):
	return HttpResponse("<h1>Branch Detail Page</h1>")
def BrLang_view(*args, **kwargs):
	return HttpResponse("<h1>Branch Language Page</h1>")
def Brow_view(*args, **kwargs):
	return HttpResponse("<h1>Browser Page</h1>")
def CapEditSign_view(*args, **kwargs):
	return HttpResponse("<h1>Capture/Edit Signature Page</h1>")
def CenMetDate_view(*args, **kwargs):
	return HttpResponse("<h1>Center Meeting Date Page</h1>")
def ChgCID_view(*args, **kwargs):
	return HttpResponse("<h1>Change CID Page</h1>")
def ChgCIDApp_view(*args, **kwargs):
	return HttpResponse("<h1>Change CID Approval Page</h1>")
def ChgIntMode_view(*args, **kwargs):
	return HttpResponse("<h1>Change Interest Mode Page</h1>")
def ChgIntRate_view(*args, **kwargs):
	return HttpResponse("<h1>Change Interest Rate Page</h1>")
def ChgSinTory_view(*args, **kwargs):
	return HttpResponse("<h1>Change Signatories Page</h1>")
def ChgUserPass_view(*args, **kwargs):
	return HttpResponse("<h1>Change User Password Page</h1>")
def Chrg_view(*args, **kwargs):
	return HttpResponse("<h1>Charges Page</h1>")
def ChrOfAcc_view(*args, **kwargs):
	return HttpResponse("<h1>Chart of Accounts Page</h1>")
def ChqPrVoid_view(*args, **kwargs):
	return HttpResponse("<h1>Print Voided Cheque Page</h1>")
def ChqPrLoan_view(*args, **kwargs):
	return HttpResponse("<h1>Print Loan Cheque Page</h1>")
def ChqPrLoanA_view(*args, **kwargs):
	return HttpResponse("<h1>Print Loan Cheque Page</h1>")
def ChqPrLoanApr_view(*args, **kwargs):
	return HttpResponse("<h1>Print Loan Cheque Approval Page</h1>")
def ChqBook_view(*args, **kwargs):
	return HttpResponse("<h1>Cheque Book Page</h1>")
def ChqBookCan_view(*args, **kwargs):
	return HttpResponse("<h1>Cancel Cheque Book Page</h1>")
def ChqDep_view(*args, **kwargs):
	return HttpResponse("<h1>Cheque Deposit Page</h1>")












































