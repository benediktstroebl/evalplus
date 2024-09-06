
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # your code here
    if x % 2 != 0 or y % 2 != 0:
        return -1
    if x % 2 == 0:
        num = x
    if y % 2 == 0:
        num = y
    if x > y:
        return -1
    else:
        for i in range(num, y, 2):
            if i > num:
                num = i
                break
            else:
                num = num
    return num

