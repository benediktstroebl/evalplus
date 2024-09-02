
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x = str(x)
    if shift == 0:
        return x
    y = ""
    for i in range(len(x)):
        y = y + x[i - shift]
    if shift > len(x):
        y = y[::-1]
    return y

