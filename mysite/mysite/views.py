#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
import datetime

def inicio(request):
	return HttpResponse("Pagina de inicio")

def hola(request):
	return HttpResponse("Hola a todos")
	
def fecha_actual(request):
	now = datetime.datetime.now()
	# t = get_template('plantilla_fecha_actual.html')
	# #html = "<!DOCTYPE html><html><head><title>Fecha</title></head><body>La fecha actual es: %s.</body></html>" % now
	# html = t.render(Context({'fecha_actual': now}))
	# return 	HttpResponse(html)
	return render_to_response('plantilla_fecha_actual.html', {'fecha_actual': now})
	
def fecha_horas_adelante(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	#assert False
	html = "<!DOCTYPE html><html><head><title>Fecha</title></head><body>Dentro de %s hora(s) la fecha ser&aacute: %s</body></html>" % (offset, dt)
	return 	HttpResponse(html)