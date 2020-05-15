from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'hithere':'This is me'})

def count(request):
    fultext = request.GET['fultext']
    wordlist = fultext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to worddictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fultext':fultext,'count':len(wordlist),'sortedwords':sortedwords})

def eggs(request):
    return HttpResponse('<h1>Eggs are Great!<h1/>')

def about(request):
    return render(request, 'about.html')
