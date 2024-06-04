from django.http import HttpResponse #importar modulo

# Create your views here.
def saludos(request): #Funcion
    return HttpResponse("Bienvenido")

def servicio(request):
    return HttpResponse('Servicio') # Aqui se añade la nueva funcion.
