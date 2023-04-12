import pyperclip as clip
import os
import sys


def main():
    argv = sys.argv
    
    try:
        if argv[1] == "-h":
            print(help_text)
        
        elif argv[1] == "-c":
            path = argv[2]
            copier(path)

        elif argv[1] == "-we":
            path = argv[2]

        else:
            print(help_text)
            
    except:
        print(help_text)


def copier(path):
    with open(path,"r") as f:
        copy_string = f.read()
        clip.copy(copy_string)
        print("Congratulation")

help_text = """
-h : help
-c [pathfile] : copy the file 
"""


if __name__ == "__main__":
    main()
