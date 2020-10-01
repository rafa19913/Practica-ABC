from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from abcapp.models import Registros, Marcas, Presentacion


def registros(request):
    no_registros_var = Registros.objects.count()
    registros = Registros.objects.all()

    marcas = Marcas.objects.all()
    presentaciones = Presentacion.objects.all()


    return render(request,'registros.html',{'no_registros': no_registros_var,'registros': registros,'marcas': marcas, 'presentaciones': presentaciones})




def nuevo(request):

    if request.method == 'POST':
        id_marca = request.POST['marca']
        id_presentacion = request.POST['presentacion']
        registro = Registros.objects.create(marca_id=id_marca,presentacion_id=id_presentacion)
        registro.save()
        return redirect('/')

    else:
        marcas = Marcas.objects.all()
        presentaciones = Presentacion.objects.all()

        return render(request,'nuevo.html',{'marcas': marcas, 'presentaciones': presentaciones})


def editarRegistro(request):

    if request.method == 'POST':
        id_marca = request.POST['marcaselect']
        id_presentacion = request.POST['presentacionselect']
        id_registro = request.POST['id']

        r = Registros.objects.get(id=id_registro)
        r.marca_id = id_marca
        r.presentacion_id = id_presentacion
        r.save()

        return redirect('/')

def eliminarRegistro(request):
    id_registro = request.POST['idEliminarRegistro']
    registro = get_object_or_404(Registros, pk=id_registro)
    registro.delete()
    return redirect('/')




