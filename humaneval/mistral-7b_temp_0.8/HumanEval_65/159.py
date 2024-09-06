
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    """
    s = str(x)
    for i in range(shift):
        s = s[1:] + s[0]
    return s
    """

    x = str(x)
    n = len(x)
    s = x
    for i in range(shift):
        if shift > n:
            x = x[-1] + x[:-1]
        else:
            x = x[-shift:] + x[:-shift]
    return x
