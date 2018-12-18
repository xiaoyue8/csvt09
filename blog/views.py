# Create your views here.
from django.shortcuts import render_to_response,HttpResponse
from django import forms

class UserForm(forms.Form):
	username = forms.CharField()
	headImg = forms.FileField()

def register(req):
	if req.method == "POST":
		uf = UserForm(req.POST,req.FILES)
		if uf.is_valid():
			print uf.cleaned_data
			return HttpResponse('ok')
	else :
		uf = UserForm()	
	return render_to_response('register.html',{'uf':uf})