#!/usr/bin/env python3
"""
This program takes a species list, gets an image from bioweb
and saves it in a folder called images.
Images are taken from [BIOWEB](https://bioweb.bio/) 
using [BIOWEB REST API](https://bioweb.bio/developer/).
Before proceding please review and agree with the
[data usage conditions](https://bioweb.bio/portal/Datos/UsoDatos/).
"""

# Created date: 13-08-2022
# Author: Karen Loaiza

# Libraries
from myfunctions import get_images


# Main
with open('species.txt', 'r') as infile:
    for line in infile:
        species = line.strip()
        get_images(species, 'images')
