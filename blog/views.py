# Create your views here.
from django.shortcuts import render_to_response


def register(req):
	return render_to_response('register.html',{})