from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA =  {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home_view(request):
    recipe = {}
    for rec in DATA:
        recipe[rec] = rec
    context = {
        'recipe': recipe
    }

    return render(request, 'calculator/home.html', context)
def recipes(request):
    count_pers = int(request.GET.get('servings', 1))
    recipe = {}
    key_ = request.build_absolute_uri().split('/')[3]
    one_recipe = DATA[key_]
    for rec, am in one_recipe.items():
        recipe[rec] = am * count_pers
    context = {
      'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)
