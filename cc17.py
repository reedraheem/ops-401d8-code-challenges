#! /usr/bin/python 3

#Reference: Chat Gpt Assisted

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
#Successfully connect to the VirusTotal API
#Automatically compare your target file’s md5 hash with the hash values of entries on VirusTotal API
#Print to the screen the number of positives detected and total files scanned
#The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.

import os
import hashlib
import requests

def calculate_md5(file_path):
    """Calculate MD5 hash of a file."""
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def scan_file_with_virustotal(api_key, file_path):
    """Scan a file using VirusTotal API."""
    url = "https://www.virustotal.com/api/v3/files"
    headers = {
        "x-apikey": api_key,
    }

    md5_hash = calculate_md5(file_path)
    params = {
        "checksum": md5_hash,
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    positives = data["data"]["attributes"]["last_analysis_stats"]["malicious"]
    total = data["data"]["attributes"]["last_analysis_stats"]["total"]

    return positives, total

def main():
    api_key = "0e21d353d30719e5c0f552b4d0216e2acbca66e85d7e5c8a31679f97ae5ce09e"
    target_file = "C:\Users\reeds\Documents\virustotal.py"
    
    if not os.path.exists(target_file):
        print("Target file not found.")
        return

    positives, total = scan_file_with_virustotal(api_key, target_file)
    
    print(f"Positives detected: {positives}")
    print(f"Total files scanned: {total}")

if __name__ == "__main__":
    main()
