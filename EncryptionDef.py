from Converting_Str_Num import *

m= 100746831503809
e= 65537
d= 47502589681765
n= 822439

privk = d
pubk = e
c= (m**e) % n


def encrypt_1(g):
    g= (g**e) % n
    print(g)

    return g

def decrypt_1(f):
    f = (f**d) % n
    print(f)
    return f
