from PIL import Image
import pillow_heif
import os

def convert(heic):
    heif_file = pillow_heif.read_heif(heic)
    name = heic.replace('heic', 'jpeg')
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        )
    image.save(name, format("jpeg"))

obj = os.scandir(os.getcwd())
for entry in obj:
    if entry.is_file():
        
        if entry.name.lower().endswith('.heic'):
            print(entry.name)  
            convert(entry.name)   