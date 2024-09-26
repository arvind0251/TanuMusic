import os
import logging
import sys
from os import listdir, mkdir

from config import TEMP_DB_FOLDER
from ..logging import LOGGER


def dirr():
    assets_folder = "assets"
    downloads_folder = "downloads"
    cache_folder = "cache"

    if assets_folder not in listdir():
        logging.warning(
            f"{assets_folder} Folder not Found. Please clone or fork repository again."
        )
        sys.exit()
        
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)
        elif file.endswith(".mp3"):
            os.remove(file)
        elif file.endswith(".session"):
            os.remove(file)
        elif file.endswith(".session-journal"):
            os.remove(file)
            
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    if "TEMP_DB_FOLDER" not in os.listdir():
        os.mkdir("TEMP_DB_FOLDER")
    

    LOGGER(__name__).info("❖ Directories Updated...🧡")
