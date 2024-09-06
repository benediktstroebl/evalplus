
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # return str(int(str(x)[1:]+str(x)[0]))
    s = str(x)
    r = s[shift:] + s[:shift]
    return r if len(r) == len(s) else r[::-1]
    # x = str(x)
    # return str(int(x[shift:] + x[:shift])) if len(x) == len(x[shift:] + x[:shift]) else str(int(x[shift:] + x[:shift])[::-1])

