#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import logging
from pathlib import Path

# Get paths
here = Path(__file__)
libDirectory = str(here.parent / 'lib')
pictureDirectory = str(here.parent.parent / 'data' / 'dist')

# Imports
sys.path.append(libDirectory)
from waveshare_epd import epd7in5_V2
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)

try:
    epd = epd7in5_V2.EPD()
    epd.init()
    epd.Clear()

    Himage = Image.open(os.path.join(pictureDirectory, 'black-dragon.jpg'))
    epd.display(epd.getbuffer(Himage))

except IOError as e:
    print(e)

sys.exit(libDirectory)
