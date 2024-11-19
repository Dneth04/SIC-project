# SIC-project
# Marine Debris Detection using U-Net

## Overview
This project focuses on detecting and segmenting marine debris from underwater sonar images using a U-Net model with a VGG16 backbone. The dataset includes various types of debris, and the model is trained to segment these objects accurately using semantic segmentation techniques.

## Requirements
- Python 3.x
- TensorFlow
- Keras
- OpenCV
- Streamlit

## Dataset
The dataset consists of 1868 sonar images and 1868 corresponding masks. The images are used for training a U-Net model, which segments different types of marine debris. The dataset includes 11 distinct classes of objects, such as:
- Wall
- Can
- Drink-carton
- Tire
- Valve
- Bottle
- Shampoo-bottle
- Propeller
- Hook
- Chain
- Standing-bottle

## Model Details
- **Architecture**: U-Net with VGG16 backbone (pre-trained on ImageNet).
- **Loss Function**: Binary Cross-Entropy with Dice coefficient as an evaluation metric.
- **Optimizer**: Adam (learning rate 0.0001).
- **Epochs**: 40 epochs with early stopping.
- **Evaluation Metrics**: Mean Intersection over Union (IoU) and Dice Similarity coefficient.

### Results
[Presentation](https://docs.google.com/presentation/d/1OCtkn9_Ov9S3pKEpCA8YQ-z2CdTvdKrxsobB_-r00ok/edit?usp=sharing)
[Model](https://www.kaggle.com/models/dumplinghead/vgg16)
IoU (Training Set): 0.5351
IoU (Validation Set): 0.5353
Dice Similarity (Test Set): 0.8571


