
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_s = str(x)
    x_l = len(x_s)
    x_l_s = str(x_l)
    x_l_l = len(x_l_s)
    shift %= x_l
    if x_l <= shift:
        x_s = x_s[shift:]
        x_s += x_s[:shift]
    elif shift != 0:
        x_s = x_s[:-shift]
        x_s += x_s[-shift:]
    x_s = x_l_s + x_s
    return x_s

