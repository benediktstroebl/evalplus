
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
        # If y is even, just return it
        if y % 2 == 0:
            return y
        # If y is odd, subtract 1 and check again
        else:
            return choose_num(y-1, y)
    # If y is less than x, just return the biggest even number in the range
    else:
        # Check for numbers that are evenly divisible by 2
        for i in range(x, y+1):
            if i % 2 == 0:
                return i
        # If no such number is found, return -1
        return -1
