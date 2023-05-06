from django.shortcuts import render


def main(request):
    title = "Карточки"

    content = {"title": title}

    return render(request, "mainapp/main_page.html", content)
