from django.shortcuts import render, HttpResponse
# from transformers import pipeline
# emotion = pipeline('sentiment-analysis',model='arpanghoshal/EmoRoBERTa')
import random
import speech_recognition as sr
from playsound import playsound
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def mymood(request):
    return render(request, 'mymood.html')

def mainpage(request):
    data = request.POST.get('name')
    print(data)
    l=["How have you been feeling this week?","What happened over your weekend","Is there anything bothering you",
    "How do you feel about yourself?","Describe yourself in a sentence"]
    context={'variable':random.choice(l)}
    # print(type(context_dict)) 
    return render(request, 'mainpage.html',context)

def mycode(request):
    data = request.POST.get('name')
    # emotion_labels = emotion(data)
    # print(emotion_labels[0]['label'])
    # print(data)
    context={'variable':data}
    # print(context)
    # print("joker")
    if context=="":
         print("start")
    #      playsound('D:\\song Recommender\\MoodRecognizer\static\\neutral\\Kuch Baatein Payal Dev 128 Kbps.mp3')
    #      print("stop")
    return render(request,'mymood.html',context)

def mycode1(request):
    data = request.POST.get('name')
    # r=sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("hi Speaking")
    #     audio=r.listen(source)

    #     try:
    #         text=r.recogize_google(audio)
    #         # emotion_labels = emotion(text)
    #         # print(emotion_labels[0]['label'])
    #         context={'variable':text}
    
    #     except:
    #         print("sry speak again")
    print("Hi preeti")
    return HttpResponse("helo")
    # return render(request,'mymood.html',context)
    

    



