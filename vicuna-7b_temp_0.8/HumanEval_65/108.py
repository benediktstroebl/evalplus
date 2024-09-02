
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    sign = 1 if x < 0 else -1
    x = int(x)
    y = 0
    while x:
        x, y = y, x % y
    return sign * '0' * (shift - len(str(x))) + str(x)
