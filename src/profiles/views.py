from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def home(request):
	context = locals()
	template = 'home.html'
	return render(request,template,context)

'''def JobPage(request):
	context = locals()
	template = 'JobPage.html'
	return render(request,template,context)'''

# Create your views here.
