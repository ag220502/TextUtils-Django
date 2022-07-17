
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.POST.get('text', 'default')
    remPunc= request.POST.get('remPunc', 'off')
    uppCase = request.POST.get('uppCase', 'off')
    lineRem = request.POST.get('lineRem', 'off')
    exSpRem = request.POST.get('exSpRem', 'off')
    print(lineRem)
    print("hello")
    if remPunc == "on":
        text = removePunct(request,text)
    if uppCase == 'on':
        text = upCase(request, text)
    if lineRem == 'on':
        print("in new")
        text = newLineRem(request, text)
        print(text)
    if exSpRem == 'on':
        text = exSpaceRem(request, text)
    params = {'analyzedText': text}
    return render(request, 'analyze.html', params)

def exSpaceRem(request, text):
    anText = ''
    for index, char in enumerate(text):
        if not(text[index] == " " and text[index+1] == " "):
            anText = anText + char
    return anText


def newLineRem(request,text):
    anText = ''
    for char in text:
        if char!="\n" and char!="\r":
            anText = anText + char
    return anText

def removePunct(request,text):
    anText=''
    listPunc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    for char in text:
        if char not in listPunc:
            anText = anText + char
    return anText

def upCase(request,text):
    anText=''
    for char in text:
        anText = anText + char.upper()
    return anText