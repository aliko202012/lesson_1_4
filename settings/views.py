from django.shortcuts import render

# Create your views here.
def settings (request):
    context ={
        "title" : "Абдурахманов Азизбек"
        "description" : "Ученик 4 месяца"

    }
    return render (request, "index.html", context = context)