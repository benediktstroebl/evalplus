
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    
    # convert to string
    x = str(x)
    
    # get length of number
    N = len(x)
    
    # circular shift the digits of x by shift
    i = 0
    while (N >= shift):
        x = x[1:] + x[:1]
        i = i+1
        N = N-1
    
    # return the result as a string
    return x
