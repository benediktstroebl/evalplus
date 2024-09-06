
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    for num in range(x+1, y):
        if num % 2 == 0:
            return num
    return -1


assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(12, 19) == 16
assert choose_num(15, 17) == -1
assert choose_num(13, 19) == 18
assert choose_num(7, 19) == -1
assert choose_num(7, 19) == -1

