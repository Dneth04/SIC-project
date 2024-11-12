import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import base64
# Load the saved model
 
@st.cache_resource # Caches the loaded model to speed up future loads
def load_model():
 return tf.keras.models.load_model('12_11.h5')
unet_model = load_model()


# Function to convert image to base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Set the background of the Streamlit app (for both app and sidebar)
def set_background(image_path):
    base64_image = get_base64_of_image(image_path)
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{base64_image}");
        background-size: cover;
        background-repeat: no-repeat; 
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)
def set_bag(image_path):
    base64_image = get_base64_of_image(image_path)
    bag = f"""
    <style>   
    .css-1d391kg {{
        background: url("data:image/jpeg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        color: white;
    }}
    </style>
    """
    st.markdown(bag, unsafe_allow_html=True)


# Set background using the local image
set_background("8e8c72a1459ad7332b14306bea1af865.gif")  # Replace with your local image path
set_bag("bg-app.jpg")  # Replace with your local image path
# Preprocess the uploaded image to match the model's input shape
def preprocess_image(image, target_size=(160, 160)):
 # Ensure image is in RGB format (convert if not)
 image = image.convert("RGB")
 image = image.resize(target_size) # Resize image to match model's expected input
 image_array = np.array(image)   # Normalize to [0, 1] range
 image_array = np.expand_dims(image_array, axis= 0) # Add batch dimension: (1, 160, 160, 3)
 st.write("Shape of preprocessed image"+ str(image_array.shape))
 return image_array
# # Function to process and return the segmentation mask
# def get_segmentation_mask(prediction):
# # Remove extra dimensions and ensure the prediction is in the right format
# prediction = np.squeeze(prediction)
# # Scale to [0, 255] for visualization
# prediction = (prediction * 255).astype(np.uint8)
# return prediction
# Streamlit app

st.title("Image Segmentation App")
# Streamlit app
st.markdown(
    """
    <h1 style='color: #083875;'>Semantic Segmentation of Marine Debris using Sonar Imaging</h1>
    """,
    unsafe_allow_html=True
)
st.markdown("<h4 style='color: #00000;'>An SIC Capstone project by Terrapix</h4>", unsafe_allow_html=True)

# Add custom styling to the sidebar with a GIF background
st.markdown(""" 
    <style>

        /* Style for Links in the Sidebar */
        .css-1d391kg a {
            font-size: 20px;  /* Slightly larger font for links */
            text-decoration: none;  /* Remove underline */
        }

        /* Change color of links when hovered */
        .css-1d391kg a:hover {
            color: #1ABC9C;  /* Greenish link color on hover */
            font-weight: bold;  /* Bold links on hover */
        }

        /* Sidebar Header Styling */
        .css-1d391kg h1 {
            color: #E74C3C;  /* Highlight header color */
            font-size: 24px;
            font-weight: bold;
        }

        /* Styling the Sidebar Items */
        .css-1d391kg li {
            margin-bottom: 15px;
        }

        /* Style the Sidebar Section Links with Emojis */
        .css-1d391kg li a {
            font-size: 18px;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Content
st.sidebar.write("## Menu")
st.sidebar.markdown("""
    **Navigate to:**
    - 🏠 [Home](#home)
    - 🌊 [Motivation](#motivation)
    - 🔬 [Demo](#demo)
""", unsafe_allow_html=True)

st.markdown('  \n<h2 id="motivation" style="color: #F9F6EE;"> Motivation </h2>', unsafe_allow_html=True)
st.markdown("<p style='text_align:left; font-weight: bold;'>The identification and categorization of underwater debris remain critical challenges in marine conservation, often hampered by limitations in robotic imaging tools. These tools frequently struggle to capture clear images in underwater environments, complicating the detection and segmentation of debris necessary for targeted cleanup efforts. Inspired by sustainability initiatives and ocean cleanup organizations, this project aims to address these challenges by developing a semantic segmentation model tailored for underwater debris identification. By enhancing the accuracy and ease of debris detection, this model seeks to support efficient cleanup operations and contribute to the broader goal of sustainable marine ecosystem preservation.</p>", unsafe_allow_html=True)

st.markdown('  \n<h2 id="demo" style="color: #F9F6EE;"> Demo</h2>', unsafe_allow_html=True)

upload_img_container= st.container()

with upload_img_container: 
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    submit= st.button(label= "Predict mask")

#display outputs
container= st.container()

with container:
    col1,col2= st.columns(2)
    with col1:
        orig_img= st.image([])
    with col2:
        pred_img= st.image([])

if uploaded_file is not None and submit==True:
 # Load the image
     image = Image.open(uploaded_file) 
     
     # Preprocess and predict
     st.write("Processing image and predicting...")
     input_image = preprocess_image(image)
     prediction = unet_model.predict(input_image)
     # st.write(prediction.shape)
     # prediction= np.expand_dims(prediction, axis=)
     # Get the segmentation mask
     # mask = get_segmentation_mask(prediction)
     # Display the mask
     orig_img.image(input_image, caption="Uploaded Image", use_column_width=True)
     pred_img.image(prediction[0], caption="Segmentation Mask", use_column_width=True,channels="GRAY")