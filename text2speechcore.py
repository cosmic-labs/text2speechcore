import os

def start():
    print("Text2Speech - Make sure you use quotations! Type :end to end!")
    print
    while True:
        a = str(input(">"))
        if (a == ":end"):
            break
        a = "say " + a
        os.system(a)

start()
