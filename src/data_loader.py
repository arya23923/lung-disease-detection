import kaggle
import zipfile
import os

# Set directories
DATA_RAW_DIR = "data/raw"
os.makedirs(DATA_RAW_DIR, exist_ok=True)

# Download the dataset
kaggle.api.dataset_download_files("nih-chest-xrays/sample", path=DATA_RAW_DIR, unzip=True)

print("Dataset downloaded and extracted to:", DATA_RAW_DIR)
