# Fruit Classification using Deep Learning and Flask
This project utilizes computer vision and deep learning techniques to classify different types of fruits from images. The implemented Flask web application allows users to upload an image of a fruit, and the system will identify and display the type of fruit in the image.

## Table of Contents
1) Project Overview
2) Folder Structure
3) Installation
4) Usage
5) Web Interface
6) Model

## Project Overview
This project demonstrates the use of deep learning and Flask, a Python web framework, to classify five types of fruits: apple, banana, orange, pineapple, and watermelon. The neural network model is constructed using TensorFlow and consists of convolutional layers for feature extraction and fully connected layers for classification.

## Folder Structure
The project has the following folder structure:

dataset/ - Contains the training, testing, and validation data.<br>
images/ - Initial dataset before splitting.<br>
static/ - Holds JavaScript and CSS files for the web interface.<br>
templates/ - Contains the HTML template for the web interface.<br>
uploads/ - Temporary directory to store user-uploaded images.<br>
app.py - Main Flask application file.<br>
fruit_classification_model.h5 - Pre-trained model weights.<br>
README.md - This readme file.<br>

## Installation
Install the required Python libraries:<br>

```sh
pip install flask tensorflow numpy
```
  
## Usage
Navigate to the project directory in your terminal.

Run the Flask application:<br>
* npm
  ```sh
  pip install flask tensorflow numpy
  ```
Open a web browser and go to http://127.0.0.1:5000/ to access the web interface.

## Web Interface
The web interface allows users to upload an image of a fruit. Upon uploading, the system processes the image and provides the predicted type of fruit. Follow these steps:

Click the "Choose File" button and select an image file.<br>
Click the "Upload & Identify" button.<br>
The system will display the predicted fruit type below the image.<br>

## Model
The deep learning model for fruit classification is built using TensorFlow. It consists of the following layers:

Convolutional layer with 32 filters and ReLU activation.
MaxPooling layer.
Convolutional layer with 64 filters and ReLU activation.
MaxPooling layer.
Convolutional layer with 128 filters and ReLU activation.
MaxPooling layer.
Flatten layer.
Dropout layer with a rate of 0.5.
Fully connected layer with 128 units and ReLU activation.
Output layer with 5 units and softmax activation for multi-class classification.
