from django.http import HttpResponse
import datetime
from django.template import Template, Context

def login(request): # Vista login
    
    doc_externo=open('./core/plantillas/login.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def home(request): # Vista Home
    
    doc_externo=open('./core/plantillas/login.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)