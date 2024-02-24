# Problem Statement
The aim of the work is to perform detection and classification of plastic present in rivers using YOLO V8 and Detectron 2.
 Determining the geographical location of detected waste i.e plastic with the help of parameters which includes latitude and longitude.

# Motivation
The management and preservation of ecosystems, natural resources etc are essential in order to ensure that they remain sustained for future generations. The material like plastic which itself being versatile and durable becomes hazardous in many ways. Plastic items often end up in landfills or rivers where they can persist for hundreds of years causing harm to ecosystems, marine life inside water etc. Aquatic animals often mistake plastic debris for food. When ingested, plastic can block their digestive systems, causing malnutrition, starvation and death. Plastic waste on the ocean floor or in coral reefs can damage these habitats, affecting the species that rely on them. Even plastics present in rivers can absorb concentrate pollutants from surrounding water and when the same is ingested by marine organisms they can suffer from toxic effects. The presence of plastic in water bodies can disrupt food chains and marine ecosystems, leading to imbalances and decreased biodiversity. So, taking into consideration all the above impacts of plastic presence in water bodies, it becomes important to detect the presence of this hazardous material inside rivers. The motive of this work is to perform the detection and classification of plastic from rivers using YOLO V8 and Detectron 2. In addition to it our work focuses on determining the geographical location of detected waste i.e plastic, so that same can be removed from that particular location.

# Work Plan
Our work plan involves following steps:
Dataset collection with the help of capturing of images from a drone.
Data preprocessing which involves flipping, tilting etc of images. This step is performed for the purpose of data augmentation.
Applying Yolo V8 and Detectron 2 on the dataset to get inference rules . The one that provides the best result is taken into consideration via which we can detect the plastic objects present in an image and perform classification of detected plastic objects.
Once the plastic object is detected and classified we will try to find the geographical location of the same object so that later on such a kind of object can be removed from that particular location.

As already discussed above, the harmful effects of plastic present in rivers. In regard to this our work will somehow help to first detect the plastic object present in the river and determine the geographical location of detected plastic object. This will help in removing such objects from that particular location which inturn leads to  preservation of aquatic life and preventing water bodies from being polluted due to plastic.

# Future Work
1.Our future work focuses on developing a hybrid model of YOLO V8 and Detectron 
2. This hybrid model will consist of a combination of features extracted by YOLO V8 and Detectron 2 which will further improve the process of detection and classification of plastic objects present on rivers. 



# References:
1)G. Aldric Sio, D. Guantero and J. Villaverde, "Plastic Waste Detection on Rivers Using YOLOv5 Algorithm," 2022 13th International Conference on Computing Communication and Networking Technologies (ICCCNT), Kharagpur, India, 2022, pp. 1-6, doi: 10.1109/ICCCNT54827.2022.9984439.
2)@article{article,
author = {Salman, Ahmad and Ali, Mouiad},
year = {2021},
month = {08},
pages = {},
title = {Comparative Study: 2D object Detection & inferencing using Detectron2}
}
