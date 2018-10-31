from tkinter import *
from EncryptionDef import *
from Converting_Str_Num import *
from bytes_to_int import *
#   Set the root and the geometry
root = Tk()
print(root)
root.geometry('400x400')

#   Create a label
Encryptkeylb = Label(root, text='E')
Encryptkeylb.grid(row=0)

Decrytpkeylb = Label(root, text='D')
Decrytpkeylb.grid(row=1)


#   Create an Entry
Encryptionk = Entry(root, width=10)
Encryptionk.grid(row=0, column=1)

Decrytionk = Entry(root, width=10)
Decrytionk.grid(row=1, column=1)


#   Create a Text
etxt = Text(root, width=10, height=1)
etxt.grid(row=0, column=2)
etxt.insert(END, 'text here')

dtxt = Text(root, width=10, height=1)
dtxt.grid(row=1, column=2)
dtxt.insert(END, 'moar text')


#   define a "call back function" for the button click
def do_encryption(event=None):
    etxt.delete(1.0, END)
    ecry = Encryptionk.get()
    ecry = STR_nums(ecry)
    printedencry = encrypt_1(ecry)
    print(printedencry)
    etxt.insert(END, printedencry)

def transfer():
    transferval = etxt.get(1.0, END)
    print(transferval)
    Decrytionk.insert(END, transferval)

#this tends to spaz, ask Mr. Kim?
def do_decryption():
    dtxt.delete(1.0, END)
    decry = Decrytionk.get()
    print(decry)
    decry = int(decry)
    print(decry)
    decry = decrypt_1(decry)
    print(decry)
    Decryption.insert(END, decry)


# define the button
EncryptBut = Button(root, text='Encrypt', command = do_encryption)
EncryptBut.grid(row=3)

TransBut = Button(root, text='Transfer', command = transfer)
TransBut.grid(row = 4)

DecryptBut = Button(root, text= 'Decrypt', command = do_decryption)
DecryptBut.grid(row = 5)

#   Run the main loop
root.mainloop()
