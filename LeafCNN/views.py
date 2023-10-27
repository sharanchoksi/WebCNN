from django.shortcuts import render
from joblib import load
import numpy as np
import tensorflow as tf
from django.conf import settings
from django.core.files.storage import default_storage

# from django.http import HttpResponse

model=load('./savedModels/model.joblib')



# Create your views here.
def Welcome(request):
    return render(request,'home.html')

def Signup(request):
    return render(request,'signup.html')

def Login(request):
    return render(request,'login.html')

def Mainpage(request):
    return render(request,'mainpage.html')

def Contact(request):
    return render(request,'contact.html')

# def Results(request):
#     return render(request,'results.html')

def Predictor(request):
    if request.method == "POST":
        file = request.FILES["imageFile"]
        file_name=default_storage.save(file.name,file)
        file_url=default_storage.path(file_name)
        class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
        img = tf.keras.preprocessing.image.load_img(file_url, target_size=(256,256))
        inputimg_array = tf.keras.preprocessing.image.img_to_array(img)
        print(inputimg_array.shape)
        img1=inputimg_array.reshape((1,256,256,3))
        print(img1.shape)
        inputimg_pred = model.predict(img1)
        pred_label = class_names[np.argmax(inputimg_pred)]
        print(pred_label)
    else:
        # This handles GET requests or any other request method
        print('No image file provided in the request')

    return render(request, 'results.html', {'prediction':pred_label})