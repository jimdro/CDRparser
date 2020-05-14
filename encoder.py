"""
Created by Dimitrios Drosos at 12/05/2020
email: dimitriss.drosos@gmail.com
"""
import asn1
import subprocess
from shutil import copyfile
import os, sys, stat
from schema import Schema
import time

def main():
    project = []
    project_name = str(input("Give the name of your project: "))
    project.append(project_name)
    print(project)

    cdr_name = str(input("Give the name of your cdr which you like to encode: "))
    if cdr_name == '' or cdr_name == 'null':
        print("Give correct name")
    else:
        print("Exit")

    f = open(cdr_name, "r")
    print(f.read())

    # try:
    #     f = open(cdr_name, "r")
    # except:
    #     print("Give a valid txt file or you haven't gave anything as an input")
    #
    # print(f.read())

    # Encoding_process
    f = asn1.Encoder()
    f.start()
    f.write('1.2.3', asn1.Numbers.ObjectIdentifier)
    final = f.output()

    # Create new file for encoded
    encoded = open("final_new.AIR", "w+")
    encoded.write(str(final))
    print(encoded.read())

    filepath = os.path.join("/home/project/encodedFiles","berfile")
    if not os.path.exists("/home/project/encodedFiles"):
        os.makedirs("/home/project/encodedFiles")

    os.chmod("/home/project/encodedFiles/final_new.AIR", stat.S_IRWXO)
    os.chown("path", "root", "root")
    copyfile('/home/project/encodedFiles/*.txt', '/tmp/xxxxxx/incoming/ADJUSTMENTS/')


if __name__ == "__main__":
    main()