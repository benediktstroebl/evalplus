
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    start = x
    end = y
    while start <= end:
        mid = (start + end) // 2
        if mid % 2 == 0:
            return mid
        elif mid < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1
