
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    shift = shift % len(x)
    if shift == 0:
        return x
    s = ""
    for i in range(shift):
        s = x[i] + s
    for i in range(len(x) - shift):
        s = s + x[i + shift]
    return s

