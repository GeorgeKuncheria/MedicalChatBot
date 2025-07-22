import os
from pathlib import Path
import logging


# File for creating directories and files if they do not exist
# To run "python template.py" in the terminal
# Add file paths to the list_of_files variable



logging.basicConfig(level=logging.INFO,format='[%(asctime)s] :%(message)s: ')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "trials.py"
]


for filepath in list_of_files:
    filepath = Path(filepath) # Convert to Path object in respecitve operative system
    filedir,filename = os.path.split(filepath)


    if filedir!="":
        logging.info(f"Creating directory: {filedir} for file: {filename}")
        os.makedirs(filedir,exist_ok=True) #exist_ok=True allows the directory to be created if it does not exist

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating file: {filename}")
            
            
    else:
        logging.info(f"File already exists: {filename}")


