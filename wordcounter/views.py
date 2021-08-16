from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request,'home.html')

def submit_one(request):
	tex = request.GET['ftext']
	word_list = tex.split()
	return render(request,'countletters.html',{'ftext' : tex ,'count': len(word_list)})

def about_info(request):
	return render(request,'info_about.html')

	