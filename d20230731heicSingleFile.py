from PIL import Image
import pillow_heif

#Heic Resmi jpg'e çeviren fonksiyon.

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


convert("sample1.heic")   