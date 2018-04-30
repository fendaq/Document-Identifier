#Using google vision api to identify the doc 
import io
import os
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

credential = config['DEFAULT']['cred']

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import credentials


# Instantiates a client
client = vision.ImageAnnotatorClient(credentials = credential)

# The name of the image file to annotate
file_name = 'resources/1.jpg'

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)

