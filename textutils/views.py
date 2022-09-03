# create this file by Kishu
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'project.html', )


def textutil(request):
    message = request.POST.get('text', 'default')
    check1 = request.POST.get('check1', 'default')
    check2 = request.POST.get('check2', 'default')
    check3 = request.POST.get('check3', 'default')
    check4 = request.POST.get('check4', 'default')
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    if check1 == 'on':
        analyzed = ''
        for char in message:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        message = analyzed

    if check2 == 'on':
        analyzed = ''
        for char in message:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Lower Case to Upper Case', 'analyzed_text': analyzed}
        message = analyzed

    if check3 == 'on':
        analyzed = ''
        for char in message:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        message = analyzed

    if check4 == 'on':
        analyzed = ''
        for index, char in enumerate(message):
            if not (message[index] == " " and message[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
    if check1 != 'on' and check2 != 'on' and check3 != 'on' and check4 != 'on':
        return render(request, 'error.html')
    else:
        return render(request, 'analyze.html', params)


def error(request):
    return render(request, 'error.html')


def search(request):
    searching = request.POST.get('search1', 'default')
    if searching == 'analyze':
        return render(request, 'analyze.html')
    else:
        return render(request, 'error.html')
