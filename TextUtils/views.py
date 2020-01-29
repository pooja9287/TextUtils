from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index2.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('caps', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    if removepunc == "on":
        punctuations = '''!~`@#$%^&*()_+-={}[]:";'<>?,.//*-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if capitalize=="on":
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params = {'purpose': 'Capitalize all the characters', 'analyzed_text': analyzed}
        djtext = analyzed
    if extraspace=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed+char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
    if newlineremover=="on":
      analyzed=""
      for char in djtext:
          if char !="\n" and char !="\r":
              analyzed = analyzed+char
          else:
              print("no")
      print("pre", analyzed)
      params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
    if(removepunc != "on" and extraspace!="on" and newlineremover!="on" and capitalize!="on"):
        return HttpResponse("PLEASE SELECT ANY OPERATION AND TRY AGAIN...")

    return render(request, 'analyzed2.html', params)


