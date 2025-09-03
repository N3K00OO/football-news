from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406434153',
        'name': 'Gregorius Ega Aditama Sudjali',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
