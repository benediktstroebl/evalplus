
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    xstr = str(x)
    if len(xstr) == 0:
        return "0"
    out = xstr[0]
    if len(xstr) == shift:
        return out
    for i in range(len(xstr) - shift):
        out += xstr[i + shift]
    return out[::-1]
