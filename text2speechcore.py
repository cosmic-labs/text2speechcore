import os

def start():
    print("Text2Speech - Make sure you use quotations!")
    print
    while True:
        a = str(input(">"))
        a = "say " + a
        os.system(a)

start()
