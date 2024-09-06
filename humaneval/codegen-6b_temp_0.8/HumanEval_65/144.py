
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n = len(str(x))
    mod = shift % n
    res = x
    if shift >= n:
        res = int(str(x)[mod:] + str(x)[:mod])
    else:
        res = int(str(x)[n-mod:] + str(x)[:n-mod])
    return str(res)

