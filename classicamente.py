import random
import os

def encrypt(data):
    n=4
    cols = [data[i::n] for i in range(n)]
    return "".join(cols)


flag = "f{anuiraaso_lfltnfi_sin_aime_rotpze_gne_ca_roi}_"
enc = encrypt(flag)
while True:
    enc=encrypt(enc)
    print(enc)
    if "flag" in enc:
        os.system("pause")