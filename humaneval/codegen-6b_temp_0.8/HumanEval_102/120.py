
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    i = x
    while (i < y):
        if is_even(i) == True:
            return i
        i += 1
    return -1

x = int(input("Enter x: "))
y = int(input("Enter y: "))