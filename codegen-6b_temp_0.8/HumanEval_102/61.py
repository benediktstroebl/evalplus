
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x <= 0 or y <= 0:
        return -1
    if y % 2 == 1:
        return -1
    if x > y:
        return -1
    if x == y:
        return x
    if x < y:
        x = y
    max_int = 0
    min_int = 0
    num = 1
    while True:
        if num <= x:
            if num % 2 == 0 and num > max_int:
                max_int = num
            if num % 2 == 1 and num > min_int:
                min_int = num
        if num == y:
            return max_int
        num += 1

