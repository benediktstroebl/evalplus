
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2 != 0 and y % 2 != 0:
        return -1
    else:
        return x if x%2==0 else y

assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(10, 30) == 22
assert choose_num(30, 26) == 24
assert choose_num(5, 4) == -1
assert choose_num(0, 3) == -1
assert choose_num(2, 10) == -1
assert choose_num(48, 49) == 48
assert choose_num(1, 1) == 1
assert choose_num(3, 5) == -1
assert choose_num(4, 2) == 4
assert choose_num(17, 8) == -1