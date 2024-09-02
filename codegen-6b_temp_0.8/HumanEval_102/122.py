
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if type(x) != int or type(y) != int:
        raise TypeError("Only integers are allowed")
    if x < 0 or y < 0:
        raise TypeError("Only positives are allowed")
    if x % 2 != 0 or y % 2 != 0:
        raise ValueError("Only even numbers are allowed")
    i = max(max(math.ceil(x/2), math.floor(y/2)), 1)
    if i > y:
        return -1
    else:
        return i*2


