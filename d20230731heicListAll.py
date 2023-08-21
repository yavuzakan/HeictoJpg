import os

obj = os.scandir(os.getcwd())
for entry in obj:
    if entry.is_file():
        
        if entry.name.lower().endswith('.heic'):
            print(entry.name)  
         
         
