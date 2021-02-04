from PIL import Image
import requests
import sys
import os

second_arg = sys.argv[2]
quality = sys.argv[3]

def read(directory=second_arg,q=quality):
 
    os.chdir(directory)
    files = os.listdir()
    images = [file for file in files if file.endswith(('jpg','jpeg'))]
    for image in images:
    
        foo = Image.open(image)
        dimension = float(os.stat(image).st_size)/1024
        foo.save("New_"+ image, optimize=True, quality = int(q)) 
        dimension_new = float(os.stat("New_" + image).st_size)/1024
        print ("Original Size: " + str(round(dimension, 2)) + " kb" + " ---> " + "New Size: "+ str(round(dimension_new, 2)) + " kb")
        
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2],sys.argv[3])

