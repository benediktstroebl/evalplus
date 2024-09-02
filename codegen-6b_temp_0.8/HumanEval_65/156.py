
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert type(x) is int and x >= 0
    assert type(shift) is int and shift >= 0
    s = str(x)
    l = len(s)
    if shift > l:
        return s[::-1]
    return s[shift % l:] + s[:shift % l]
