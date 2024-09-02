
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    if (x / 2) == int((x / 2)):
        while True:
            if ((x % 2) == 0) and (y % 2) == 0:
                x = int((x - 1) / 2)
            else:
                break
    elif (x / 2) > int((x / 2)):
        if x % 2 == 0:
            x = x / 2
        else:
            x = (x + 1) / 2
        
    if (y / 2) == int((y / 2)):
        while True:
            if ((y % 2) == 0) and (x % 2) == 0:
                y = int((y - 1) / 2)
            else:
                break
    elif (y / 2) > int((y / 2)):
        if y % 2 == 0:
            y = y / 2
        else:
            y = (y + 1) / 2
    
    if (x <= y):
        return -1 
    elif (x > y):
        return ((x - 1) * ((y - 1) / 2)) + ((y + 1) / 2)

