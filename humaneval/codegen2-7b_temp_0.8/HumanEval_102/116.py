
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    while True:
        x = random.randint(x, y)
        y = random.randint(x+1, y)
        if is_even(x) and is_even(y):
            return x, y
