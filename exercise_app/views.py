from django.shortcuts import render

# Create your views here.
def dynamic_url(request, pk):
    pk=pk
    return render(request, 'index.html', {'pk':pk})
    