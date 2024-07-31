path = r"ENTER THE PATH HERE...!"


def Encrypt():
    key = int(input("Enter the key: "))
    print("path of the file:",path)
    print("key for encrypt: ",key)

    f1=open(path,"rb")

    image=f1.read()
    f1.close()

    image = bytearray(image)

    for index, value in enumerate(image):
        image[index]=value^key

    f1=open(path,"wb")
    f1.write(image)
    f1.close()
    print("Encryption done")

def Decrypt():
            key = int(input("Enter the key for decryption: "))
            print("path of the file:",path)
            print("key for decrypt: ",key)

            f1=open(path,"rb")

            image=f1.read()
            f1.close()

            image = bytearray(image)

            for index, value in enumerate(image):
                image[index]=value^key

            f1=open(path,"wb")
            f1.write(image)
            f1.close()
            print("Decryption done")
  
while True:
    choise=input("Enter the choise, 0 for Encryption and 1 for Decryption...!\nEnter 8 for quit the program...!")
    if choise=="0":
        Encrypt()
    else:
        Decrypt()
    if choise=="8":
        break