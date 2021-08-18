from os import system

print("""
For Debian \"Linux\" [1]
For Windows [2]
""")
number = input("==>")
if number == "1":
    system("sudo apt update && sudo apt install python3-pip && pip3 install pafy")
    print("""

Done..""")
elif number == "2":
    system("pip install pafy")
else:
    print("Error.")

