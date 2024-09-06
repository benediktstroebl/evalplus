
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    biggest_num = 0
    for number in range(x, y+1):
        if number % 2 == 0 and number > biggest_num:
            biggest_num = number
    if biggest_num == 0:
        return -1
    else:
        return biggest_num

