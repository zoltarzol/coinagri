from django.shortcuts import render
from .functions import squared
# Create your views here.

def home_view(request):
    weekdays = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]
    context = {
            'test' : "Ceci est un test",
            'carre_6' : squared(6),
            'weekdays' : weekdays
    }

    import pudb; pu.db()

    return render(request,'divers/home_page.html', context=context)