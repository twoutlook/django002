from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 欠料")
    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)