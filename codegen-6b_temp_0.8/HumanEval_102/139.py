
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # CHALLENGE: What is 'x' and 'y'
    
    # x = 14
    # y = 17
    
    # numbers are even
    if x % 2 == 0 and y % 2 == 0:
        # both numbers are even
        if y > x:
            # biggest even integer is between x and y
            return (y - x)/2
        else:
            # biggest even integer is between y and x
            return (x - y)/2
    else:
        # x and y are both odd, so there's no biggest even integer
        return -1
    