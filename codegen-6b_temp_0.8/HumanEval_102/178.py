
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2 == 0:
        end = x-1
    else:
        end = x
    if y // 2 == 0:
        begin = y-1
    else:
        begin = y
    while begin <= end:
        mid = (begin + end) // 2
        if mid % 2 == 0:
            if x <= mid <= y:
                return mid
            elif y < mid:
                end = mid - 1
            else:
                begin = mid + 1
        else:
            if x <= mid:
                end = mid - 1
            else:
                begin = mid + 1
    return -1

