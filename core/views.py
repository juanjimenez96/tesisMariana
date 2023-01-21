from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): # primera vista

    doc_externo=open("G:/trabajo tesis mariana/env/core/plantillas/login.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)

    return HttpResponse(documento)

