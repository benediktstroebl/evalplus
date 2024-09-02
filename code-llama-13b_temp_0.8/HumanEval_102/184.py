
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y or x <= 0 or y <= 0:
        return -1
    
    if y - x <= 1:
        return y
    
    middle = (x + y) // 2

    if middle % 2 == 1:
        middle += 1

    if middle < x or middle > y:
        return -1

    return middle
