from os import system, name
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def while_loop (my_loop):
    counter = 0
    while(counter < len(my_loop)):
        print (my_loop[counter])
        counter -= 1

def for_loop (my_loop):
    for one_item in my_loop:
        print (one_item)

def my_mag(loop_type):
    print("$$$$$$$$$$$$$$$$")
