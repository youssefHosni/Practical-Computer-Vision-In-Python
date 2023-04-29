import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
from keras_contrib.layers.normalization.instancenormalization import InstanceNormalization 
import numpy as np
from numpy import  vstack 

#loading pretrained GAN models 
cust = {'InstanceNormalization':InstanceNormalization}
model_horse2zebra = load_model('./g_model_AtoB_023740.h5',cust)
model_zebra2horse = load_model('./g_model_BtoA_023740.h5',cust)


def load_image(image_path):
    """
    Function to load image given image path
    :param image_path: image path 
    :return: loaded image
    """
    image = Image.open(image_path)
    newsize = (256, 256)
    image = image.resize(newsize)
    image = np.array(image)
    image = image[np.newaxis, ...]  # convert the array into 3D array
    return image

def generate_image(model, image):
    """
    Function to generate image 
    :param model: the GAN model to generate new image
    :param image: the image to 
    :return: generated images
    """
    generated_image = model.predict(image)
    images = vstack(generated_image)
    images = (images+1)/2.0
    return images

st.title("Horse Zebra GAN Web APP") # Set the title  
st.image(Image.open('./1.png'))

pick = st.selectbox("Please select a GAN model to use:", ["Horse 2 Zebra GAN", "Zebra 2 Horse GAN"])

if pick == "Horse 2 Zebra GAN":
    st.write("This is a GAN model for Generating Zebra images from Horses")
    st.write("Try out the GAN model with a default images of a horse or simply upload an image")

    if st.button("Try with Default Image"):
        image = load_image('./horse.jpg')
        st.subheader("Horse Image")
        st.image(image)
        st.subheader("Generated Zebra Image")
        st.image(generate_image(model_horse2zebra, image))

    st.subheader("Upload an image file of a horse to convert it to a Zebra")
    uploaded_file = st.file_uploader("Upload JPG image file of a horse only", type=["jpg","jpeg"])

    if uploaded_file:
        image = load_image(uploaded_file)
        st.image(generate_image(model_horse2zebra, image))

elif pick == "Zebra 2 Horse GAN" :
    st.write("This is a GAN model for Generating Horse images from Zebras")
    st.write("Try out the GAN model with a default images of a zebra or simply upload an image")

    if st.button("Try with Default Image"):
        image = load_image('./zebra.jpg')
        st.subheader("Zebra Image")
        st.image(image)
        st.subheader("Generated Horse Image")
        st.image(generate_image(model_zebra2horse, image))

    st.subheader("Upload an image file of a zebra to convert it to a horse")
    uploaded_file = st.file_uploader("Upload JPG image file of a zebra only", type=["jpg","jpeg"])

    if uploaded_file:
        image = load_image(uploaded_file)
        st.image(generate_image(model_zebra2horse, image))
        

