from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    length = len(word_list)
    worddictionary={}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word]+=1

        else:
            worddictionary[word]=1

    return render(request,'count.html',{ 'fulltext' : data,'words':length,'worddictionary':worddictionary.items()})
