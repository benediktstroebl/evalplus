
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        print("The first parameter is bigger than the second one.")
        return

    while not (y%2 == 0 and x%2 == 0):
        if y%2 != 0:
            y -= 1
        else:
            x += 1
    print("The biggest even number in the range [{} , {}] inclusive is {}".format(x,y,x))
