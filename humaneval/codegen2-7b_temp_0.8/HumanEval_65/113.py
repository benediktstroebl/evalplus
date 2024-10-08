
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert shift >= 0
    n = len(str(x))
    s = str(x)
    if shift > n:
        return s[-n:] + s[:-n]
    return s[-shift:] + s[:-shift]

