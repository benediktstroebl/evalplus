
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x <= 0 or y <= 0 or x > y:
        return -1

    min_number = max(x, y) if x < y else min(x, y)
    max_number = min(x, y) if x > y else max(x, y)

    for number in range(max_number, min_number-1, -2):
        if number <= max_number and number >= min_number:
            return number

    return -1

