
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift == 0:
        return x
    while len(str(x)) < shift:
        x *= 10
    return str(int(x) // (shift // 2)) + str(x % (shift // 2))[::-1]