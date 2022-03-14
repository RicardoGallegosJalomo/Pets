from django.shortcuts import render, redirect
from .models import DatosGrales
from .forms import DatosForm

def home(request):

	datos = DatosGrales.objects.all()
	context = {'datos':datos}
	return render(request, 'crud/home.html', context)

def agregar(request):

	if request.method == "POST":
		form = DatosForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = DatosForm()
		
	context = {'form': form}
	return render(request, 'crud/agregar.html', context)

def eliminar(request,id):
	iddelete = DatosGrales.objects.get(id=id)
	iddelete.delete()
	return redirect("home")

def editar(request, id):
	idedit = DatosGrales.objects.get(id=id)
	if request.method == "POST":
		form = DatosForm(request.POST, instance=idedit)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = DatosForm(instance=idedit)

	context = {"form": form}
	return render(request, "crud/editar.html", context)