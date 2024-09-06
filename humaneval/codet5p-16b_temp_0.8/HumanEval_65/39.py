
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    res = list(str(x))
    if shift > len(res):
        return "".join(res[::-1])
    else:
        return "".join(res[-shift:] + res[:-shift])
    
