from PIL import Image
from PRFE import *

def bin_to_text(tab):
    return ''.join(chr(int(x,2)) for x in tab)

def decode(image,key=""):
    pixels = image.load()
    bin_data = []
    current_string = ""
    iteration = 0
    length = 0
    length_string = ""
    text_for_debug = ""
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            for p in range(len(pixels[i,j])):
                if iteration<16:
                    if pixels[i,j][p]%2==0:
                        length_string += "0"
                    else:
                        length_string += "1"
                    
                elif pixels[i,j][p]%2==0:
                    current_string += "0"
                    text_for_debug += "0"
                else:
                    current_string += "1"
                    text_for_debug += "1"
                    
#                 if len(current_string) == 8:
#                     bin_data.append(current_string)
#                     current_string = ""
                iteration +=1
                
                if len(length_string)==16:
                    length = int(length_string,2)
                    #print(length)
                    
                
                
                if iteration == length+16:
                    current_string = decrypter(current_string,key)
                    return current_string[:len(current_string)-1]
    
def image_print(image):
    for i in image.getdata():
        print(i)


def encode(text,image,key=""):
    pixels = image.load()
    text = text + "x"
    text = ''.join(format(x,'08b') for x in bytes(text,"ansi"))
    print(f"text len is {len(text)}")
    text = encrypter(text,key)
    print(f"text len is {len(text)}")
    length = len(text)
    length = format(length,'016b')
    iteration = 0
   
    text = length+text
    print(text)
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            print(pixels[i,j])
            tmp = list(pixels[i,j])
            
            for k in range(len(tmp)):
                if iteration == len(text)-1:
                    return image
                
                elif text[iteration]=="0":
                    if tmp[k]%2!=0:
                        if tmp[k]==255:
                            tmp[k]-=1
                        else:
                            tmp[k]+=1
                            
                            
                elif text[iteration]=="1":
                    if tmp[k]%2==0:
                        tmp[k]+=1
                        
                iteration +=1
                
            image.putpixel((i,j),tuple(tmp))
    
            
                        

