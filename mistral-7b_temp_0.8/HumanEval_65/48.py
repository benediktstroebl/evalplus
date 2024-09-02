
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    #shift = shift % len(x)
    n = 0
    if shift > len(x):
        n = 1
        shift = shift % len(x)
    i = 0
    while i < shift:
        x = x[1:] + x[0]
        i += 1
    return x if n == 0 else x[::-1]
    #return x[n:] + x[:n]
