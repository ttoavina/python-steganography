from PIL import Image


def decode(image):
    data = image.getdata()
    bin_data = []
    current_string = ""
    for pixels in data:
        for pixel in pixels:
            if pixel%2 == 0:
                current_string +="0"
            else:
                current_string +="1"

            if len(current_string)==8:
                #print(current_string)
                bin_data.append(current_string)
                current_string = ""
    return bin_data

def encode(text,image):
    #image.show()
    #for im in image.getdata():
        #print(im)

    pixels = image.load()
    text = ''.join(format(x,'b') for x in bytes(text,"ascii"))
    print(text)
    iteration = 0

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            
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


            pixel = tuple(tmp)
            image.putpixel((i,j),pixel)
            print(f"pixel : {pixels[i,j]}")
    

                        



if __name__ == "__main__":
    img = Image.open("C:/Users/Toavina/Pictures/Crypto/icon.PNG")
    
    img = encode("test_data",img)

    #New pixel
    for pixel in img.getdata():
        print(pixel)
    