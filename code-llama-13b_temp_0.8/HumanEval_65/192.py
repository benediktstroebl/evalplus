
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert to str
    x = str(x)
    # if shift is greater than length of x, return reverse of x
    if shift > len(x):
        return x[::-1]
    # if shift is negative, return as is
    if shift < 0:
        return x
    # get slice
    return x[-shift:] + x[:-shift]

