
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    d = str(x)
    l = len(d)
    if shift > l:
        shift = shift%l
    if shift >= l//2:
        return d[l-shift:] + d[:l-shift]
    else:
        return d[shift:] + d[:shift]


