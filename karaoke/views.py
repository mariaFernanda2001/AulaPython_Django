from django.shortcuts import render

# Create your views here.
def index(request):
    # contexto permiter criar uma variável
    context = {
        'nomes':[
            'mafe',
            'quel',
            'patty'
        ],
        'vazio': False,
        'teste': 'teste'}

    return render(request, "index.html", context)
