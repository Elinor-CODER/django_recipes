from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
}
def recipes(request, name):
    if name in DATA:
        data = DATA[name]
        servings = request.GET.get('servings', None)

        if servings:
            result = dict()
            for item, value in data.items():
                new_value = value * int(servings)
                result[item] = new_value
            context = {
                'name': name,
                'recipe': result
            }
    return render(request, "index.html", DATA)