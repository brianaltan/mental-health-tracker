from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152166',
        'name': 'Brian Altan',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)