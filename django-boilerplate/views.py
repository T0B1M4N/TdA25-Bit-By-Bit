from django.http import JsonResponse

def api_view(request):
    data = {"message": "Student Cyber Games"}
    return JsonResponse(data)
