# HDL-Progressive-Resizing-and-PCA-for-Cervical-Cancer-Detection

Public Datasets utilized for Cervical Cancer Detection:

SIPAKMED DATA: https://www.cs.uoi.gr/~marina/sipakmed.html 

LBC DATA: https://data.mendeley.com/datasets/zddtpgzv63/4

# Steps to Run the Python code

**Resizing the data**
1. Ensure Git is Installed:
Make sure that Git is installed on your computer. You can download and install Git from the official Git website.

2. Add Git to Your System PATH:
During the installation process, ensure you check the option to "Add Git to PATH". This allows Git to be run from any command prompt or script.

3. Check if Git is Recognized by the System:
Open the Command Prompt and type:
git –version

4. Run the Python script:

  data_resizing.py

  Now the resized data is stored with the folder names “SIPaKMeD_224x224”, “SIPaKMeD_512x512”, and “SIPaKMeD_1024x1024” in the current directory.


**Data division**

The dataset with different sizes is divided into training, validation, and testing with 60%, 20%, and 20% proportions.
Run the Python script:

data_divison.py


**Data Augmentation**

The training data stored in the folders “SIPaKMeD_224x224”, “SIPaKMeD_512x512”, and “SIPaKMeD_1024x1024” get augmented by using 10 augmentation functions.
Run the Python script:

data_augmentation.py


**Feature Extraction**

For feature extraction using ResNet152 and VGG16 run the following python script:

resnet152_features.py

vgg16_features.py

Each algorithm is analyzed for 3 iterations. In iteration 1, models utilized “SIPaKMeD_224x224” data, for iteration 2, they used “SIPaKMeD_224x224 and SIPaKMeD_512x512” data and lastly in iteration 3 performance is measured on “SIPaKMeD_224x224, SIPaKMeD_512x512, and SIPaKMeD_1024x1024” data. The weight files from the three iterations of each models are stored as ‘resnet152_iteration1.h5’, ‘resnet152_iteration2.h5’, and ‘resnet152_iteration3.h5’ for VGG16; and ‘vgg_iteration1.h5’, ‘vgg_iteration2.h5’, and ‘vgg_iteration3.h5’ for VGG16.


**Feature Concatenation**

For feature concatenation of weight files of ResNet152 and VGG16 for each iterations run the following python script: 

feature_concatenation.py

The concatenated features set are obtained as 'concatenate_model1.h5', 'concatenate_model2.h5', and 'concatenate_model3.h5' for the three iterations respectively.


**PCA for Dimensionality Reduction**

To reduce the dimension of concatenated features, PCA is implemented. Run the following Python code:

pca_application.py

The reduced features set obtained are 'pca_weights_reduced1.npy', 'pca_weights_reduced2.npy', and 'pca_weights_reduced3.npy' for the three iterations respectively.


**Classification using Majority Voting Classifier using SVM and RF**
SVM and RF are used for classification of pap smear test data for three different resolutions. The classification decision is based on the majority vote of two classifiers. 
Run the following Python script for the classification report:

classification_svm_rf.py

