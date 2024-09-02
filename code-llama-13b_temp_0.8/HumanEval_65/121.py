
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
    s = shift % n
    d = 10 ** s
    a = (x // d)
    b = (x % d)
    if s == 0:
        return str(x)
    else:
        return str(b * (10 ** (n-s)) + a)
