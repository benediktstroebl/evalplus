
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    numbers = list(range(x, y))
    result = []
    for n in numbers:
        if n % 2 == 0 and n > 0:
            result.append(n)
    if result == []:
        return -1
    else:
        return max(result)

