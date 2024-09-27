import os
import logging
import sys
from os import listdir, mkdir

from config import TEMP_DB_FOLDER
LOGGER = logging.getLogger(__name__)

def dirr():
    print(f"Current working directory: {os.getcwd()} 💙")
    
    assets_folder = "TanuMusic/assets"
    downloads_folder = "downloads"
    cache_folder = "cache"

    # Check if assets folder exists; if not, create it
    if not os.path.exists(assets_folder):
        os.makedirs(assets_folder)
        LOGGER.info(f"Created missing folder: {assets_folder} 💾")
    else:
        LOGGER.info(f"{assets_folder} exists ✔️")
        
    # Remove specific file types
    for file in os.listdir():
        if file.endswith((".jpg", ".jpeg", ".png", ".mp3", ".session", ".session-journal")):
            os.remove(file)
            
    # Create folders if they don't exist
    if not os.path.exists(downloads_folder):
        os.mkdir(downloads_folder)
    if not os.path.exists(cache_folder):
        os.mkdir(cache_folder)
    if not os.path.exists(TEMP_DB_FOLDER):
        os.mkdir(TEMP_DB_FOLDER)
    
    LOGGER.info("❖ Directories Updated...🧡")
