"""
Created by Dimitrios Drosos at 12/05/2020
"""
import asn1
import subprocess
from shutil import copyfile
import os, sys, stat

def main():
    try:
        f = open("AIROUTPUTCDR_4006_XPKABJM01_3518_20200313-175940.AIR.txt", "r")
    except:
        print("Give a valid txt file or you haven't gave anything as an input")

    print(f.read())

    # Encoding_process
    f = asn1.Encoder()
    f.start()
    f.write('1.2.3', asn1.Numbers.ObjectIdentifier)
    final = f.output()

    # Create new file for encoded
    encoded = open("final_new.txt", "w+")
    encoded.write(str(final))
    print(encoded.read())

    filepath = os.path.join("/home/project/encodedFiles","berfile")
    if not os.path.exists("/home/project/encodedFiles"):
        os.makedirs("/home/project/encodedFiles")

    os.chmod("/home/project/encodedFiles/final_new.txt", stat.S_IRWXO)
    os.chown("path", "root", "root")
    copyfile('/home/project/encodedFiles/*.txt', '/tmp/cdrs-id_indosat_vad/incoming/ADJUSTMENTS/')


if __name__ == "__main__":
