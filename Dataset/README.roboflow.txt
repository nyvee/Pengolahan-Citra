
Red-Green-Blue Detection of a Traffic Light - v3 2024-11-12 10:39pm
==============================

This dataset was exported via roboflow.com on March 2, 2025 at 1:10 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 206 images.
Merah-kuning-hijau are annotated in YOLOv12 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise
* Randomly crop between 0 and 50 percent of the image
* Random rotation of between -45 and +45 degrees
* Random shear of between -14° to +14° horizontally and -15° to +15° vertically
* Random brigthness adjustment of between -23 and +23 percent
* Random exposure adjustment of between -12 and +12 percent
* Random Gaussian blur of between 0 and 2.5 pixels


