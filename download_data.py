import os
import zipfile

os.environ['KAGGLE_CONFIG_DIR'] = os.path.join(os.getcwd(), 'env')
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

dataset_name = "sameep98/housing-prices-in-mumbai"
output_dir = './dataset'  

os.makedirs(output_dir, exist_ok=True)

print(f"Downloading dataset: {dataset_name}")
api.dataset_download_files(dataset_name, path=output_dir, unzip=True)

print("✅ Dataset downloaded and extracted successfully.")
