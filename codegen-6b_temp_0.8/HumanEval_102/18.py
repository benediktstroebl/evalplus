
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    x = int(x)
    y = int(y)
    if y < x:
        temp = x
        x = y
        y = temp
    biggest_number = 0
    while x <= y:
        if x % 2 == 0:
            print(x)
            if x > biggest_number and x < y:
                biggest_number = x
            x += 1
            
        else:
            x += 1
    if biggest_number == 0:
        return -1
    else:
        return biggest_number
   