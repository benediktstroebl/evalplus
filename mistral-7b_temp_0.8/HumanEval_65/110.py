
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = ""
    for i in range(x):
        s += str(i)
    i = 0
    while i < shift:
        s = s[1:] + s[0]
        i = i + 1
    return s
