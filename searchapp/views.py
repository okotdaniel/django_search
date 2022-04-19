from django.shortcuts import render
from django.db.models import Q
from searchapp.models import Todo
# Create your views here.
def index(request):

   
    results = []

    if request.method == "GET":
        query = request.GET.get('search', '')

        if query == '':
            query = "None"
        results = Todo.objects.filter(Q(title__contains=query))
    

    return render(request, "index.html" ,{ 'results': results, 'query': query})