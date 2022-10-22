from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("welocome to Django ORM, my first ever django app")