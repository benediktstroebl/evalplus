
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    def is_even(n):
        return n % 2 == 0

    while(True):
        if is_even(x) and is_even(y):
            if x > y:
                break
            else:
                y -= 2
                continue
        elif is_even(x) and not is_even(y):
            y -= 1
            continue
        elif not is_even(x) and is_even(y):
            x -= 1
            continue
        else:
            break

    return x if x > y else y
