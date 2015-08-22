from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from .models import Person
from .forms import RegistForm

# Create your views here.
def Home(request):
	return render(request, 'home.html')

def Register(request):
	if request.method == 'POST':
		
		form = RegistForm(request.POST)

		if form.is_valid():
			a = form.cleaned_date['username']
			b = form.cleaned_date['password']
			Person.objects.create(username = a,password = b)
			return HttpResponse('regist success!')

	else:
		form = RegistForm()
	return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))

def RegisterDone(request):
	return render(request, 'registerdone.html')

