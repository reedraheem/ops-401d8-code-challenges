#! /usr/bin/python 3



# Script:   code challenge 16         
# Author: Raheem Sharif Reed                     
# Date of latest revision: August 22,2023      
# Purpose:prompt the user to type in a file name to search for
#prompt the user for a directory to search in
#search each file in the directory by name
#for each positive detection,print to the screen the file name and location
#at the end of the search process,print to the screen how many files were searched and how many hits were found.
#this script must successfully execute on both ubuntu linux 20.04 focal fossa and windows 10
#Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.
#For each file scanned within the scope of your search directory:Generate the file’s MD5 hash using Hashlib.
#Assign the MD5 hash to a variable.
#Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.
#The script should be tested to execute successfully in Python3.



import os
import platform
import hashlib
import datetime

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def search_files(directory, filename):
    hits = 0
    searched_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if filename in file:
                hits += 1
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_md5 = calculate_md5(file_path)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                print(f"Timestamp: {timestamp}")
                print(f"File Name: {file}")
                print(f"File Size: {file_size} bytes")
                print(f"File Path: {file_path}")
                print(f"MD5 Hash: {file_md5}\n")
                
            searched_files += 1
    
    return searched_files, hits

def main():
    filename = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    if platform.system() == "Windows":
        directory = directory.replace("/", "\\")

    searched_files, hits = search_files(directory, filename)

    print(f"\nSearch Summary:")
    print(f"Total files searched: {searched_files}")
    print(f"Total hits found: {hits}")

if __name__ == "__main__":
    main()
