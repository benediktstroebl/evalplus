
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
    
    if y % 2 == 0 and is_even(x):
        return y
    if x % 2 == 0 and is_even(y):
        return x
    
    def is_in_range(n, x, y):
        return (n >= x) and (n <= y)
    
    if is_in_range(x, y):
        if (x % 2 == 0 and y % 2 == 0) or (is_in_range(x, y) and x % 2 != 0):
            return max(x, y)
    return -1

