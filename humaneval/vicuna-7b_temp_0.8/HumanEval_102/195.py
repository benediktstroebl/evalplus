
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Check if y is greater than x
    if y > x:
        return x

    # Check if x is even
    if x % 2 == 0:
        # If x is even, check if it is bigger than the half of y
        if x > int(y / 2):
            return x

    # If x is odd, check if it is bigger than the square root of y
    sqrt_y = float(y) ** 0.5
    if x > int(sqrt_y):
        return x

    # If there's no even number in the range [x, y], return -1
    return -1
