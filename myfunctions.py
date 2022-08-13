"""
This function takes a species name and a path,
gets an image from bioweb and saves it in the path.
Images are taken from [BIOWEB](https://bioweb.bio/) 
using [BIOWEB REST API](https://bioweb.bio/developer/).
Before proceding please review and agree with the
[data usage conditions](https://bioweb.bio/portal/Datos/UsoDatos/).
"""

# Created date: 13-08-2022
# Author: Karen Loaiza

# Libraries
import requests
import os


# Functions
def get_images(name, path):
    scientificName = name.replace(' ', '%20')
    api_url = f"https://apibioweb.com/api/Public/Amphibia/Species/{scientificName}"
    response = requests.get(api_url)
    species_dict = response.json()
    
    # Each species_dict has 4 types of images
    # We are only interested in 3 types:
    ikeys = ['principalImage', 'secondImage', 'thirdImage']#, 'currentDistributionImage']
    n=0
    for ikey in ikeys:
        image_name = species_dict[ikey]['imageUrl']
        image_url = f"https://multimedia20stg.blob.core.windows.net/especies/{image_name}"
        img_data = requests.get(image_url).content

        # Make a friendly name for saving the image
        scientificName = scientificName.replace('%20', '_')
        n+=1
        # Save image in current dir
        if not os.path.exists(path):
            os.makedirs(path)
        with open(f'{path}/{scientificName}_{n}.jpg', 'wb') as handler:
            handler.write(img_data)
    
    
# # Test
# name = "Allobates femoralis"
# get_images(name, 'images')