# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import forms
from blog.models import User

class UserForm(forms.Form):
	username = forms.CharField()
	headImg = forms.FileField()

def register(req):
	if req.method == "POST":
		uf = UserForm(req.POST,req.FILES)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			headImg = uf.cleaned_data['headImg']
			user = User()
			user.username = username
			user.headImg = headImg
			user.save()
			print username,headImg
			return HttpResponse('ok')
	else :
		uf = UserForm()	
	return render_to_response('register.html',{'uf':uf})