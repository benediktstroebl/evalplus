
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # your code here

    if x <= 0 or y <= 0:
        return -1

    if x > y:
        return -1

    if x == y:
        return y

    start_number = x
    end_number = y

    if end_number - start_number > 1:
        if end_number % 2 == 0:
            return end_number
        if start_number % 2 == 0:
            return start_number

        return start_number + 1

    return start_number

