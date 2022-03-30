from django.shortcuts import render, HttpResponse
# from transformers import pipeline
# emotion = pipeline('sentiment-analysis',model='arpanghoshal/EmoRoBERTa')
import random
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def mainpage(request):
    data = request.POST.get('name')
    print(data)
    l=["What are you thinking right now","How do you feel","Do you like me"]
    context={'variable':random.choice(l)}
    # print(type(context_dict)) 
    return render(request, 'mainpage.html',context)

def mycode(request):
    data = request.POST.get('name')
    # emotion_labels = emotion(data)
    # print(emotion_labels[0]['label'])
    # context={'data':data}
    return HttpResponse(data)


