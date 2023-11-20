import os
import pandas as pd
from PIL import Image
from pathlib import Path
from ultralytics import YOLO
import PIL.ExifTags

# Set the path to the directory containing the images to predict
path = "/content/Plastic_Detect/Predict"

# Load the YOLO model
model = YOLO('/content/Plastic_Detect/YOLO_Custom_v8m.pt')

# Iterate through the files in the specified directory
for i, file_name in enumerate(os.listdir(path)):
    file_path = os.path.join(path, file_name)

    # Make a prediction using the YOLO model
    model.predict(source=file_path, save=True, conf=0.37)

    # Open the image using PIL
    image = Image.open(file_path)

    # Extract GPS information from the image's EXIF data
    exif_data = {PIL.ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in PIL.ExifTags.TAGS}
    gps_info = exif_data.get('GPSInfo', None)

    if gps_info is not None:
        # Extract latitude and longitude information from GPS data
        ns = gps_info[2]
        ew = gps_info[4]
        latitude = (float(ns[0] * 3600 + ns[1] * 60 + ns[2])) / 3600000
        longitude = (float(ew[0] * 3600 + ew[1] * 60 + ew[2])) / 3600000

        # Print the values of latitude and longitude for each iteration
        print(f"Image at Index {i}: Latitude = {latitude}°N, Longitude = {longitude}°E")


