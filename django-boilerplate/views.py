from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader

def api_view(request):
    data = {"organization": "Student Cyber Games"}
    return JsonResponse(data)
def main_view(rquest):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
