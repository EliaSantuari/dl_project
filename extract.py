import zipfile
import os
from tqdm import tqdm

zip_path = "./celeba.zip"
extract_path = "./datasets/"

os.makedirs(extract_path, exist_ok=True)

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    files = zip_ref.namelist()
    # tqdm crea una barra di avanzamento che si aggiorna in tempo reale
    for file in tqdm(files, desc="Estrazione in corso"):
        zip_ref.extract(file, extract_path)

print("\nEstrazione completata!")