
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    n = 0
    for c in reversed(str(x)):
        n = n * 10 + int(c)
        if shift > n:
            return str(x)[::-1]
    return str(n)[::-1]
