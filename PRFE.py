def toggle(b):
    if b == "0":
        return "1"
    else:
        return "0"
    
def bin_to_string(seq):
    print(f"seq is {seq}")
    bin_tab = [chr(int(seq[index:index+8],2)) for index in range(0,len(seq),8)]
    return "".join(x for x in bin_tab)


def encrypter(text,key=""):
    print("ENCRYPTER")
    current_key = key
    new_text = ""
    print(f"initial is {text}")   
    for i in range(len(text)):
        current_key = abs(hash(str(current_key)))
        if current_key%2 == 0:
            new_text += toggle(text[i])
        else:
            new_text += text[i]
    print(f"encrypted is {new_text}")        
    return new_text


def decrypter(text,key=""):
    print("DECRYPTER")
    current_key = key
    new_text = ""
    print(f"encrypted is {text}")
    for i in range(len(text)):
        current_key = abs(hash(str(current_key)))
        if current_key%2 == 0:
            new_text += toggle(text[i])
        else:
            new_text += text[i]
            
    print(f"initial is {new_text}") 
    return bin_to_string(new_text)