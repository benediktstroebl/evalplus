
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    a = x % 10
    b = x // 10
    if shift >= x:
        return str(a) + str(b)
    else:
        return (a + (10 + b) * shift)
